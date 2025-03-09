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
    
    # Generate Fibonacci sequence
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Calculate the actual Fibonacci numbers
    fibonacci_nums = [0]
    for i in range(1, n):
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-1])
    
    # Return the sequence in reverse order
    return list(reversed(fibonacci_nums[:n]))