from unittest.mock import Mock
import pytest

# Mocking a function
def get_data_from_api(url):
    # This function would normally make a request to the API and return the data
    pass

def test_get_data_from_api():
    get_data_from_api = Mock(return_value="mock data")
    assert get_data_from_api("http://example.com") == "mock data"


class Database:
    def save_data(self, data):
        # This method would normally save data to the database
        pass


# Mocking a method of an object
def test_save_data():
    db = Database()
    db.save_data = Mock()
    db.save_data("test data")
    # The assert_called_once_with method is used to check that db.save_data was called
    # with the correct argument.
    db.save_data.assert_called_once_with("test data")


# Mocking a whole class
def test_save_data():
    # create_autospec function is used to create a mock that has the same methods as the original Database class.
    Database = create_autospec(Database)
    db = Database()
    db.save_data("test data")
    db.save_data.assert_called_once_with("test data")
