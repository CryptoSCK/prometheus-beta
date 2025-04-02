def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a subarray with length k.
    
    Args:
        arr (list): Input array of numbers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a subarray of length k
    
    Raises:
        ValueError: If k is invalid (less than or equal to 0 or greater than array length)
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than the input array")
    
    # Initialize max sum to first k elements
    max_sum = sum(arr[0:k])
    
    # Sliding window approach
    current_sum = max_sum
    
    # Slide the window through the rest of the array
    for i in range(k, len(arr)):
        # Remove the first element of the previous window and add the next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum