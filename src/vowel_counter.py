import unicodedata
import re

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given string case-insensitively.
    
    Args:
        text (str): The input string to count vowels in.
    
    Returns:
        int: The total number of vowels (a, e, i, o, u) in the string.
    
    Examples:
        >>> count_vowels("Hello")
        2
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("python programming")
        4
    """
    # Normalize unicode characters and remove accents
    normalized_text = ''.join(
        char for char in unicodedata.normalize('NFKD', text)
        if unicodedata.category(char) != 'Mn'
    )
    
    # Define vowels (lowercase)
    vowels = set('aeiou')
    
    # Convert input to lowercase and count vowels
    return sum(1 for char in normalized_text.lower() if char in vowels and char.isalpha())