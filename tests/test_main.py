"""
Tests for the main module
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from myproject.main import greet, add_numbers


def test_greet():
    """Test the greet function"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_add_numbers():
    """Test the add_numbers function"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, 20) == 30


if __name__ == "__main__":
    test_greet()
    test_add_numbers()
    print("All tests passed!")
