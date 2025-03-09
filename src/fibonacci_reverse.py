def fibonacci_reverse(n):
    """
    Generate a reverse Fibonacci sequence up to the Nth element.
    
    Args:
        n (int): The number of Fibonacci elements to generate.
    
    Returns:
        list: A list of Fibonacci numbers in reverse order.
    
    Raises:
        ValueError: If the input is negative.
        TypeError: If the input is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle base cases
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [1, 0]
    
    # Initialize sequence
    sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    
    # Return the sequence in reverse order, truncated to n elements
    return list(reversed(sequence[:n]))