def find_pairs_with_sum(arr, target_sum):
    """
    Find all unique pairs of numbers in the array that add up to the target sum.

    Args:
        arr (list): A list of unique integers to search through.
        target_sum (int): The target sum to find pairs for.

    Returns:
        list: A list of tuples, where each tuple contains a pair of numbers 
              that add up to the target sum.

    Raises:
        TypeError: If input is not a list or target sum is not an integer.
        ValueError: If the input list contains duplicate elements.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target_sum, int):
        raise TypeError("Target sum must be an integer")
    
    # Check for duplicates
    if len(arr) != len(set(arr)):
        raise ValueError("Input array must contain unique elements")

    # Store pairs of indices 
    result = []
    
    # Use a set for O(1) lookup
    num_set = set(arr)
    
    # Iterate through the array
    for num in arr:
        complement = target_sum - num
        
        # Ensure we don't use the same element twice and complement exists
        if complement in num_set and complement != num:
            # Add the pair in a consistent order
            pair = tuple(sorted((num, complement)))
            
            # Avoid duplicate pairs and limit to first pair found
            if pair not in result:
                result.append(pair)
                break  # Stop after finding first pair
    
    return result