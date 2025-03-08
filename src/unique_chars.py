def extract_unique_chars(number_string):
    """
    Extract unique characters from a string of numbers without using built-in unique methods.
    
    Args:
        number_string (str): A string containing numbers
    
    Returns:
        str: A string containing only unique characters in the order they first appear
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input contains non-numeric characters
    """
    # Validate input
    if not isinstance(number_string, str):
        raise TypeError("Input must be a string")
    
    # Check if all characters are numeric
    if not all(char.isdigit() for char in number_string):
        raise ValueError("Input must contain only numeric characters")
    
    # If input is empty, return empty string
    if not number_string:
        return ""
    
    # Initialize result string and seen characters tracker
    result = ""
    seen = [False] * 10  # Track digits 0-9
    
    # Iterate through input string
    for char in number_string:
        # Convert character to integer index
        digit_index = int(char)
        
        # Add to result only if not seen before
        if not seen[digit_index]:
            result += char
            seen[digit_index] = True
    
    return result