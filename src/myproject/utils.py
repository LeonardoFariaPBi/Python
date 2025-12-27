"""
Example utility functions
"""


def is_even(number: int) -> bool:
    """
    Check if a number is even.
    
    Args:
        number: The number to check
        
    Returns:
        True if the number is even, False otherwise
    """
    return number % 2 == 0


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text: The input string
        
    Returns:
        The string with each word capitalized
    """
    return ' '.join(word.capitalize() for word in text.split())
