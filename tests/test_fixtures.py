# pytest tests/test_fixtures.py

import pytest

# The fixtures person and person_m are defined in conftest.py, making them reusable across multiple test files.
def test_say_hello_alice(person):
    greeting = person.say_hello()
    assert greeting == "Hello, my name is Alice and I'm 25 years old.", "Greeting message doesn't match"

def test_say_hello_mark(person_m):
    greeting = person_m.say_hello()
    assert greeting == "Hello, my name is Mark and I'm 30 years old.", "Greeting message doesn't match"