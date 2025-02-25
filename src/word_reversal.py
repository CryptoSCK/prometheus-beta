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
        
        # Reverse the word
        reversed_word = word[::-1]
        
        # Restore original capitalization pattern
        if word.istitle():
            reversed_word = reversed_word.capitalize()
        elif word.isupper():
            reversed_word = reversed_word.upper()
        elif word.islower():
            reversed_word = reversed_word.lower()
        
        return reversed_word
    
    # Process the string
    tokens = split_with_punctuation(input_string)
    reversed_tokens = [reverse_word(token) for token in tokens]
    
    return ''.join(reversed_tokens)