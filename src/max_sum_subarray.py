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
    
    # Initialize the maximum sum
    max_sum = float('-inf')
    
    # Iterate through non-overlapping subarrays
    for i in range(0, len(arr), k):
        # Check if we can form a complete subarray of length k
        if i + k <= len(arr):
            current_sum = sum(arr[i:i+k])
            max_sum = max(max_sum, current_sum)
    
    return max_sum