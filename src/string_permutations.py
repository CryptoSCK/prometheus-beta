def generate_unique_permutations(input_string):
    """
    Generate all possible unique permutations of a given string.
    
    Args:
        input_string (str): The input string to generate permutations for.
    
    Returns:
        list: A list of unique permutations of the input string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return []
    
    # Use set to ensure uniqueness
    unique_permutations = set()
    
    def backtrack(current_perm, remaining_chars):
        # If no remaining characters, add current permutation
        if not remaining_chars:
            unique_permutations.add(current_perm)
            return
        
        # Try each remaining character as the next in the permutation
        for i in range(len(remaining_chars)):
            # Choose
            new_perm = current_perm + remaining_chars[i]
            new_remaining = remaining_chars[:i] + remaining_chars[i+1:]
            
            # Explore
            backtrack(new_perm, new_remaining)
    
    # Start the backtracking process
    backtrack('', input_string)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_permutations))