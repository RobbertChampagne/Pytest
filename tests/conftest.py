import pytest
from source.fixtures import Person

@pytest.fixture
def person():
    return Person("Alice", 25)

@pytest.fixture
def person_m():
    return Person("Mark", 30)