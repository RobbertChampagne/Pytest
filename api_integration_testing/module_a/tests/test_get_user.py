# '-n 4' This option is provided by the pytest-xdist plugin, which allows you to run tests in parallel. 
# pytest -n 4 -s api_integration_testing/module_a --html=report.html
# pytest -s api_integration_testing/module_a/tests/test_get_user.py --html=report.html

import httpx
import pytest
from jsonschema import validate
from ...core.apis_info import ApiAbbreviation, apiUrls

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "first_name": {"type": "string"},
        "email": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"},
    },
    "required": ["id", "first_name", "email", "last_name", "avatar"],
}

@pytest.mark.asyncio
async def test_get_user():
    # Create an asynchronous HTTP client
    async with httpx.AsyncClient() as client:
        # Construct the URL for the API endpoint
        url = apiUrls[ApiAbbreviation.Reqres] + "/users/8"
        
        # Make an asynchronous GET request to the API
        response = await client.get(url)
        
        # Assert that the response status code is 200 (OK)
        assert response.status_code == 200

        # Extract the user data from the JSON response
        user = response.json()["data"]
        
        # Assert that the user data is a dictionary
        assert isinstance(user, dict)

        # Validate the user data against the JSON schema
        validate(instance=user, schema=user_schema)
        
        # Print the user data (for debugging purposes)
        print(user)