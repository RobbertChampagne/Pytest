# pytest -s api_integration_testing/module_a/tests/test_get_user.py

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
    async with httpx.AsyncClient() as client:
        url = apiUrls[ApiAbbreviation.Reqres] + "/users/8"
        response = await client.get(url)
        assert response.status_code == 200

        user = response.json()["data"]
        assert isinstance(user, dict)

        validate(instance=user, schema=user_schema)
        
        print(user)