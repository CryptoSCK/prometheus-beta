"""
Module for string reversal using multiple methods.

This module provides various methods to reverse a string, demonstrating 
different Python string manipulation techniques.
"""

def reverse_string_manual(s: str) -> str:
    """
    Reverse a string using manual iteration.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_builtin(s: str) -> str:
    """
    Reverse a string using built-in reversed() function.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return ''.join(reversed(s))

def reverse_string_slice(s: str) -> str:
    """
    Reverse a string using string slicing.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return s[::-1]

def reverse_string_split_join(s: str) -> str:
    """
    Reverse a string using split(), reverse(), and join() methods.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return ''.join(list(s)[::-1])

def reverse_string_recursive(s: str) -> str:
    """
    Reverse a string recursively.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty or single character string
    if len(s) <= 1:
        return s
    
    # Recursive case: move first character to end
    return reverse_string_recursive(s[1:]) + s[0]