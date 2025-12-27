"""
Tests for the utils module
"""
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from myproject.utils import is_even, capitalize_words


def test_is_even():
    """Test the is_even function"""
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False


def test_capitalize_words():
    """Test the capitalize_words function"""
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is great") == "Python Is Great"
    assert capitalize_words("UPPER lower") == "Upper Lower"


if __name__ == "__main__":
    test_is_even()
    test_capitalize_words()
    print("All tests passed!")
