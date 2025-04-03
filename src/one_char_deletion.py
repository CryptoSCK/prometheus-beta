def can_convert_by_one_deletion(word1: str, word2: str) -> bool:
    """
    Check if word1 can be converted to word2 by deleting exactly one character.
    
    Args:
        word1 (str): The first input string
        word2 (str): The target string to convert to
    
    Returns:
        bool: True if word1 can be converted to word2 by deleting one character, False otherwise
    
    Examples:
        >>> can_convert_by_one_deletion("abcd", "abc")  # delete 'd'
        True
        >>> can_convert_by_one_deletion("ab", "b")  # delete 'a'
        True
        >>> can_convert_by_one_deletion("abc", "abcd")
        False
    """
    # If lengths differ by more than 1, conversion is impossible
    if len(word1) - len(word2) != 1:
        return False
    
    # Try removing each character from word1 and check if result matches word2
    for i in range(len(word1)):
        # Create a new string by removing the character at index i
        modified_word = word1[:i] + word1[i+1:]
        
        # If the modified word matches word2, return True
        if modified_word == word2:
            return True
    
    # No single character deletion results in word2
    return False