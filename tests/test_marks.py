# pytest tests/test_marks.py
import pytest
from source.function import is_even

"""
To run only the tests marked as slow: pytest -m slow
To run all tests except those marked as slow: pytest -m "not slow"
"""

@pytest.mark.slow
def test_slow_operation():
    # This is a slow test
    pass

@pytest.mark.xfail(reason="This test is expected to fail due to bug #123")
def test_expected_to_fail():
    # This test is expected to fail
    assert 0

@pytest.mark.skip(reason="This test is skipped because feature #456 is not yet implemented")
def test_skipped():
    # This test is skipped
    pass

@pytest.mark.custom_mark(reason="This is a custom mark with a message")
def test_custom_mark():
    # This test has a custom mark
    print()
    pass

@pytest.mark.parametrize("num, expected", [
    (2, True),
    (3, False),
    (4, True),
    (5, False),
    (10, True),
    (11, False),
    (12, True),
])
def test_is_even(num, expected):
    assert is_even(num) == expected