import unicodedata

def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. This implementation is case-insensitive
    and ignores whitespace.

    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both arguments must be strings")
    
    # Normalize Unicode characters and remove accents
    def normalize(s: str) -> str:
        # Decompose characters, remove accents, convert to lowercase
        normalized = ''.join(
            char for char in unicodedata.normalize('NFKD', s.lower())
            if not unicodedata.combining(char)
        )
        # Remove whitespace
        return ''.join(normalized.split())
    
    # Normalize and compare
    cleaned_str1 = normalize(str1)
    cleaned_str2 = normalize(str2)
    
    # Check if lengths are different
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count characters in first string
    for char in cleaned_str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    # Count characters in second string
    for char in cleaned_str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2