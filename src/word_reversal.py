import re

def reverse_words_in_string(input_string):
    """
    Reverse the order of words in a string while maintaining original capitalization and punctuation.
    
    Args:
        input_string (str): The input string to be processed.
    
    Returns:
        str: A string with words reversed, preserving original capitalization and punctuation.
    
    Examples:
        >>> reverse_words_in_string("Hello World!")
        'olleH dlroW!'
        >>> reverse_words_in_string("Python is awesome.")
        'nohtyP si emosewa.'
        >>> reverse_words_in_string("a b c")
        'a b c'
    """
    # Handle None or empty input
    if input_string is None or input_string == "":
        return input_string
    
    # Split the string into words and punctuation
    def split_with_punctuation(s):
        return re.findall(r'\w+|\W+', s)
    
    # Reverse individual words while preserving case
    def reverse_word(word):
        if not word.isalpha():
            return word
        
        # Create a list of characters to handle case by case
        chars = list(word)
        
        # Generate the case pattern
        is_title = word[0].isupper() and all(c.islower() for c in word[1:])
        is_upper = word.isupper()
        is_lower = word.islower()
        
        # Reverse the characters
        reversed_chars = chars[::-1]
        
        # Restore the original case pattern
        if is_title:
            reversed_chars[0] = reversed_chars[0].upper()
            for i in range(1, len(reversed_chars)):
                reversed_chars[i] = reversed_chars[i].lower()
        elif is_upper:
            reversed_chars = [c.upper() for c in reversed_chars]
        elif is_lower:
            reversed_chars = [c.lower() for c in reversed_chars]
        
        return ''.join(reversed_chars)
    
    # Process the string
    tokens = split_with_punctuation(input_string)
    reversed_tokens = [reverse_word(token) for token in tokens]
    
    return ''.join(reversed_tokens)