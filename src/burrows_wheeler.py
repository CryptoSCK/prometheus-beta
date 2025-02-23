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
    
    # Create first column by sorting
    first_column = sorted(bwt)
    
    # Create a mapping to track character occurrences
    first_to_last = {}
    for i, char in enumerate(first_column):
        if char not in first_to_last:
            first_to_last[char] = []
        first_to_last[char].append(i)
    
    # Use a more robust reconstruction method
    n = len(bwt)
    reconstructed = []
    current_index = original_index
    
    for _ in range(n - 1):  # Exclude the terminator
        # Use the first column character at current_index
        current_char = first_column[current_index]
        reconstructed.append(current_char)
        
        # Find the next index by tracking occurrences in the BWT string
        occurrence_list = first_to_last[current_char]
        local_index = occurrence_list.index(current_index)
        current_index = bwt.index(current_char, local_index)
    
    # Reverse to get the original text
    return ''.join(reconstructed)[::-1]