# pytest tests/test_fixtures.py

import pytest
from source.fixtures import Person

@pytest.fixture
def person():
    return Person("Alice", 25)

class TestPerson:
    def test_say_hello(self, person):
        greeting = person.say_hello()
        assert (greeting == "Hello, my name is Alice and I'm 25 years old."), "Greeting message doesn't match"

    # 'person_m' fixture is not defined in this file but in conftest.py
    def test_say_hello(self, person_m):
        greeting = person_m.say_hello()
        assert (
            greeting == "Hello, my name is Mark and I'm 30 years old."
        ), "Greeting message doesn't match"
