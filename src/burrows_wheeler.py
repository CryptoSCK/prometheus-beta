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
    
    # Add a unique terminator character 
    encoded_text = text + '$'
    
    # Generate all rotations of the text
    rotations = [encoded_text[i:] + encoded_text[:i] for i in range(len(encoded_text))]
    
    # Sort the rotations lexicographically 
    sorted_rotations = sorted(rotations)
    
    # Extract the last column of sorted rotations (Burrows-Wheeler Transform)
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    # Find the index of the original string in sorted rotations
    original_index = sorted_rotations.index(encoded_text)
    
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
    
    # First, compute the LF mapping (Last to First column mapping)
    first_column = sorted(bwt)
    
    # Compute character positions
    first_pos = {}
    last_pos = {}
    for i, char in enumerate(first_column):
        if char not in first_pos:
            first_pos[char] = i
    
    for i, char in enumerate(bwt):
        if char not in last_pos:
            last_pos[char] = 0
        last_pos[char] += 1
    
    # Reconstruct the original text
    reconstructed = []
    current = original_index
    
    # Reconstruct while avoiding the terminator
    while len(reconstructed) < len(bwt) - 1:
        # Get the character in BWT at current index
        current_char = bwt[current]
        
        # Skip the terminator
        if current_char == '$':
            # Find the next occurrence if necessary
            current = bwt.index('$', current + 1) if current + 1 < len(bwt) else current
            continue
        
        # Add the character to reconstruction
        reconstructed.append(current_char)
        
        # Update current index using LF mapping
        # Get the position of this character within its group
        char_pos = first_pos[current_char]
        current = bwt.index(current_char, char_pos)
    
    # Reconstruct only the original text (without terminator)
    return ''.join(reconstructed)[::-1]