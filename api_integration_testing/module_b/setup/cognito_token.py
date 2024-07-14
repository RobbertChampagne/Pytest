import os
from dotenv import load_dotenv
import aiofiles

# Load environment variables from .env file
load_dotenv()

token_file = "TEMP_TOKEN"

async def get_cognito_token():
    async with aiofiles.open(token_file, mode="r") as f:
        return await f.read()

async def write_cognito_token():
    token = await generate_cognito_token()
    async with aiofiles.open(token_file, mode="w") as f:
        await f.write(token)

async def unlink_cognito_token():
    os.remove(token_file) # Delete the file

async def generate_cognito_token():
    # Your call to get the token here
    # ...
    # access_token = await response_token.json()
    # return f"bearer {access_token}"
    #
    # (For now get the token from the environment variables)
    token = os.getenv("CATAPIKEY")
    return token
