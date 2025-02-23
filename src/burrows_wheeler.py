def burrows_wheeler_transform(text):
    """
    Perform the Burrows-Wheeler Transform on the input text.
    
    The Burrows-Wheeler Transform is a data compression algorithm that 
    rearranges a block of data to improve compression efficiency.
    
    Args:
        text (str): The input string to transform.
    
    Returns:
        tuple: A tuple containing:
            - The transformed string (last column of sorted rotations)
            - The index of the original string in the sorted rotations
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    # Add a unique terminator character (not in the input)
    text += '$'
    
    # Generate all rotations of the text
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    
    # Sort the rotations lexicographically 
    sorted_rotations = sorted(rotations)
    
    # Extract the last column of sorted rotations (Burrows-Wheeler Transform)
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    # Find the index of the original string in sorted rotations
    original_index = sorted_rotations.index(text)
    
    return bwt, original_index

def inverse_burrows_wheeler_transform(bwt, original_index):
    """
    Perform the inverse Burrows-Wheeler Transform to recover the original text.
    
    Args:
        bwt (str): The Burrows-Wheeler transformed string
        original_index (int): The index of the original string in sorted rotations
    
    Returns:
        str: The original text before transformation
    
    Raises:
        TypeError: If inputs are of incorrect type
        ValueError: If inputs are invalid
    """
    # Validate inputs
    if not isinstance(bwt, str):
        raise TypeError("BWT input must be a string")
    
    if not isinstance(original_index, int):
        raise TypeError("Original index must be an integer")
    
    if not bwt:
        raise ValueError("BWT string cannot be empty")
    
    if original_index < 0:
        raise ValueError("Original index cannot be negative")
    
    # Create first and last columns
    first_column = sorted(bwt)
    
    # Use a more robust approach to reconstruct text
    # Create an array to map characters from first column to last column
    char_map = {}
    map_index = {}
    
    # First, create a mapping with all occurrences of characters
    for i, char in enumerate(bwt):
        if char not in char_map:
            char_map[char] = []
        char_map[char].append(i)
    
    # Prepare mapping from first column to last column
    n = len(bwt)
    next_chars = [0] * n
    
    # Reconstruct the mapping
    for i, char in enumerate(first_column):
        # Get the next available index for this character
        if char not in map_index:
            map_index[char] = 0
        
        # Get the corresponding index in the BWT string
        next_chars[i] = char_map[char][map_index[char]]
        
        # Increment the index for this character
        map_index[char] += 1
    
    # Reconstruct the original text
    result = []
    current = original_index
    for _ in range(n - 1):  # Subtract 1 to exclude the terminator
        current = next_chars[current]
        result.append(bwt[current])
    
    # Reverse to get the original text
    return ''.join(result)[::-1]