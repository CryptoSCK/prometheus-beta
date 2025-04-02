def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a non-overlapping subarray with length k.
    
    Args:
        arr (list): Input array of numbers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a non-overlapping subarray of length k
    
    Raises:
        ValueError: If k is invalid (less than or equal to 0 or greater than array length)
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than the input array")
    
    # Initialize variables
    max_sum = float('-inf')
    
    # Track last used index to ensure non-overlapping subarrays
    last_used_index = -k
    
    # Iterate through the array
    for i in range(len(arr)):
        # If we can form a complete subarray without overlapping
        if i + k <= len(arr) and i >= last_used_index + k:
            current_sum = sum(arr[i:i+k])
            if current_sum > max_sum:
                max_sum = current_sum
                last_used_index = i
    
    return max_sum