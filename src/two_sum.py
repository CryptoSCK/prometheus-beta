def find_two_sum_indices(nums, target):
    """
    Find two indices in an array that add up to a target sum.
    
    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find
    
    Returns:
        list: A list containing two indices of numbers that add up to the target,
              or an empty list if no such indices exist
    
    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If list contains non-integer elements
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Validate input types
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Validate list contents
    if any(not isinstance(num, int) for num in nums):
        raise ValueError("List must contain only integers")
    
    # Use a dictionary to store complement values and their indices
    complement_dict = {}
    
    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in dictionary
        if complement in complement_dict:
            return [complement_dict[complement], i]
        
        # Store current number and its index
        complement_dict[num] = i
    
    # Return empty list if no solution found
    return []