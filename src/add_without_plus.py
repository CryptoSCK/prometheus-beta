def add_without_plus(a, b):
    """
    Add two integers without using the + operator.
    
    Uses bitwise operations to perform addition:
    - XOR (^) handles addition without carrying
    - AND (&) detects carry bits
    - Left shift (<<) moves carry bits to the correct position
    
    Args:
        a (int): First integer to add
        b (int): Second integer to add
    
    Returns:
        int: Sum of a and b
    
    Raises:
        TypeError: If inputs are not integers
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both arguments must be integers")
    
    # Handle edge case of 0
    while b != 0:
        # Compute sum without carrying
        current_sum = a ^ b
        
        # Compute carry bits
        carry = (a & b) << 1
        
        # Update a and b for next iteration
        a = current_sum
        b = carry
    
    return a