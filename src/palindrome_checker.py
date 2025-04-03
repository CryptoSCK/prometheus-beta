def is_palindrome(input_string: str) -> bool:
    """
    Check if the given string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward.
    This implementation is:
    - Case-sensitive
    - Handles special characters and numbers
    
    Args:
        input_string (str): The string to check for palindrome property
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        False
        >>> is_palindrome("12321")
        True
    """
    # If input is not a string, raise a TypeError
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty or a single character, it's technically a palindrome
    if len(input_string) <= 1:
        return True
    
    # Compare the string with its reverse
    return input_string == input_string[::-1]