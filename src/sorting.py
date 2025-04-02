def sort_nums(numbers):
    """
    A sorting function with an intentional bug for demonstration purposes.
    
    This implementation has a known issue that will cause incorrect sorting 
    in certain scenarios.
    
    Args:
        numbers (list): A list of numbers to be sorted
    
    Returns:
        list: A partially or incorrectly sorted list of numbers
    """
    # Intentional bug: Bubble sort with a deliberate mistake
    n = len(numbers)
    for i in range(n):
        # Intentional bug: Incorrect swap condition 
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:  # Bug: Reversed comparison
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def optimal_sort(numbers):
    """
    An improved sorting implementation with optimal time complexity.
    
    Uses Python's built-in sorted() function, which implements Timsort 
    with O(n log n) time complexity.
    
    Args:
        numbers (list): A list of numbers to be sorted
    
    Returns:
        list: A sorted list of numbers in ascending order
    """
    # Return a new sorted list without modifying the original
    return sorted(numbers)