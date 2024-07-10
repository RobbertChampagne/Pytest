import asyncio
import pytest
import os
from dotenv import load_dotenv

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


