# pytest -s api_integration_testing/module_a/test_post_user.py

import requests
import pytest
from jsonschema import validate

BASE_URL = 'https://reqres.in/api/users'

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "createdAt": {"type": "string", "format": "date-time"},
    },
    "required": ["id", "createdAt"],
}

def test_post_user():
    response = requests.post(BASE_URL)
    assert response.status_code == 201

    user = response.json()
    print(user)
    # In JavaScript, this kind of data structure is called an "object", and in Python, it's called a "dictionary".
    assert isinstance(user, dict)

    # Check that the user has the required fields
    validate(instance=user, schema=user_schema)