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
    
    # Reconstruct the original text
    reconstructed = []
    current_char = bwt[original_index]
    reconstructed.append(current_char)
    
    # Tracking the number of occurrences of each character
    while len(reconstructed) < len(bwt):
        # Find the index of the current character in the first column
        count = first_column[:bwt.index(current_char)].count(current_char)
        # Find the corresponding index in the last column
        next_index = bwt.index(current_char, count)
        
        current_char = bwt[next_index]
        reconstructed.append(current_char)
    
    # Remove the terminator and reverse
    return ''.join(reconstructed[:-1])[::-1]