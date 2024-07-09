# pytest -s api_integration_testing/module_a/test_get_users.py

import requests
import pytest
from jsonschema import validate
from core.apis_info import ApiAbbreviation, apiUrls

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

def test_get_users():
    url = apiUrls[ApiAbbreviation.Reqres] + "/users?page=2"
    response = requests.get(url)
    assert response.status_code == 200

    users = response.json()['data']
    assert isinstance(users, list)

    # Check that each user has the required fields
    for user in users:
        validate(instance=user, schema=user_schema)
