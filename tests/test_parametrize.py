# pytest tests/test_parametrize.py
import pytest

def add(a, b):
    return a + b

# To test a function with multiple inputs, test_add will be run 4 times with different values of a, b, and expected.
@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (4, 5, 9), (-1, 1, 0), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected

def divide(a, b):
    return a / b