"""
Main module with example functionality
"""


def greet(name: str) -> str:
    """
    Generate a greeting message.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add_numbers(2, 3)}")
