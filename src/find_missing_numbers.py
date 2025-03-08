def find_missing_numbers(arr):
    """
    Find and return all the numbers that are missing from a given array of unique integers.
    
    Args:
        arr (list): A list of unique integers
    
    Returns:
        list: A sorted list of missing numbers in the range of the input array
    
    Raises:
        ValueError: If the input is not a list or is empty
        TypeError: If the input contains non-integer values
    """
    # Validate input
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Check for non-integer values
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Find the range of numbers
    min_num = min(arr)
    max_num = max(arr)
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_num, max_num + 1) 
        if num not in num_set
    ]
    
    return missing_numbers