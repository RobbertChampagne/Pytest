# pytest -s api_integration_testing/module_b/tests/test_get_images.py

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

async def test_get_images():
    async with httpx.AsyncClient() as client:
        url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
        response = await client.get(url)
        assert response.status_code == 200

    user = response.json()["data"]
    assert isinstance(user, dict)

    validate(instance=user, schema=user_schema)
    
    print(user)
    
