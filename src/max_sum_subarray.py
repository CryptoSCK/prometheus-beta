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
    
    # Track last used index to ensure non-overlapping
    last_used_index = -1
    max_sum = 0
    
    # Iterate to find maximum sum
    for i in range(len(arr)):
        # If current index is not part of previous subarray
        if i - last_used_index >= k:
            # Find the maximum sum k-length subarray starting at this index
            current_sum = sum(arr[i:i+k])
            max_sum = max(max_sum, current_sum)
            
            # Update last used index if we found a greater sum
            if current_sum > max_sum:
                last_used_index = i + k - 1
    
    return max_sum