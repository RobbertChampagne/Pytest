import pytest
from source.classes import Calculator, Person

"""
The tests are now methods of the TestCalculator and TestPerson classes, 
and they use self.calculator and self.person to access the instances of the classes they're testing.

setup_method is a special method that pytest calls before each test method is executed. 
We use it to create a new instance of the class we're testing. 

teardown_method is a special method that pytest calls after each test method is executed.
We use it to clean up the instance we created.

The method parameter in setup_method(self, method) and teardown_method(self, method) 
is a reference to the actual test method that is about to be executed or has just been executed. 
This can be useful if you want to do some specific setup or teardown based on the test method.
For example, you might want to set up different fixtures or mock objects depending on the test method, 
or you might want to log which test method is being run.
In most cases, you don't need to use the method parameter, and it can be omitted.
"""

class TestCalculator:
    def setup_method(self, method):
        print(f"Setting up for test {method.__name__}")
        self.calculator = Calculator()

    def teardown_method(self, method):
        print(f"Tearing down after test {method.__name__}")
        del self.calculator

    def test_add(self):
        result = self.calculator.add(1, 2)
        assert result == 3, "Expected 3"

    def test_subtract(self):
        result = self.calculator.subtract(5, 2)
        assert result == 3, "Expected 3"

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        assert result == 6, "Expected 6"

    def test_divide(self):
        result = self.calculator.divide(6, 2)
        assert result == 3, "Expected 3"

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="You can't divide by zero!"):
            self.calculator.divide(1, 0)


class TestPerson:
    def setup_method(self, method):
        self.person = Person("Alice", 25)

    def teardown_method(self, method):
        del self.person

    def test_say_hello(self):
        greeting = self.person.say_hello()
        assert (greeting == "Hello, my name is Alice and I'm 25 years old."), "Greeting message doesn't match"
