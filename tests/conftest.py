import pytest
from source.fixtures import Person

# This fixture is available to all test files in the tests directory
@pytest.fixture
def person_m():
    return Person("Mark", 30)
