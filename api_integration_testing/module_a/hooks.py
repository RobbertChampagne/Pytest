import os
from dotenv import load_dotenv
from cognitoToken import unlink_cognito_token, write_cognito_token

# Load environment variables from .env file
load_dotenv()

def pytest_sessionstart(session):
    write_cognito_token()

def pytest_sessionfinish(session, exitstatus):
    unlink_cognito_token()
