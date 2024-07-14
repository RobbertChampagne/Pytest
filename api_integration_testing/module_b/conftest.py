import asyncio
import pytest
import os
from dotenv import load_dotenv
from .setup.cognito_token import unlink_cognito_token, write_cognito_token

# Load environment variables from .env file
load_dotenv()

# scope='session' means that the fixture is called once per test session.
# If you don't specify a scope, the fixture will be called once per test function.
@pytest.fixture(scope="session")
def env():
    return os.getenv("ENVIRONMENT")

@pytest.fixture(scope="session")
def base_url(env):
    return f"https://{env}.website123.be"

# Pytest hooks like pytest_sessionstart and pytest_sessionfinish do not support asynchronous functions directly.
# You need to run the coroutine in the event loop manually.
def run_async(async_func):
    asyncio.get_event_loop().run_until_complete(async_func)
    
def pytest_sessionstart(session):
    print("Session started")
    run_async(write_cognito_token())

def pytest_sessionfinish(session, exitstatus):
    print("Session finished")
    run_async(unlink_cognito_token())
