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
    text_with_terminator = text + '$'
    
    # Generate all rotations of the text
    rotations = [text_with_terminator[i:] + text_with_terminator[:i] for i in range(len(text_with_terminator))]
    
    # Sort the rotations lexicographically 
    sorted_rotations = sorted(rotations)
    
    # Extract the last column of sorted rotations (Burrows-Wheeler Transform)
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    # Find the index of the original string in sorted rotations
    original_index = sorted_rotations.index(text_with_terminator)
    
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
    
    # Compute the LF mapping (Last to First column mapping)
    # First, count character occurrences
    char_count = {}
    lf_mapping = []
    
    # Create first column by sorting
    first_column = sorted(bwt)
    
    # Compute LF mapping
    for i, char in enumerate(bwt):
        if char not in char_count:
            char_count[char] = 0
        lf_mapping.append(first_column.index(char, char_count[char]))
        char_count[char] += 1
    
    # Reconstruct the original text
    reconstructed = []
    current = original_index
    
    # Reconstruct until terminator
    while len(reconstructed) < len(bwt) - 1:
        # Append the character from BWT
        reconstructed.append(bwt[current])
        
        # Move to the next index using LF mapping
        current = lf_mapping[current]
    
    # Reverse to get the original text
    return ''.join(reconstructed)[::-1]