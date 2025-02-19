def generate_triangle_sequence(n):
    """
    Generate the first n numbers in a Triangle Number Sequence.
    
    A Triangle Number Sequence is a sequence where each number is the sum of integers 
    from 1 to its position. For example:
    1st triangle number: 1
    2nd triangle number: 1 + 2 = 3
    3rd triangle number: 1 + 2 + 3 = 6
    4th triangle number: 1 + 2 + 3 + 4 = 10
    
    Args:
        n (int): Number of triangle numbers to generate
    
    Returns:
        list: A list of the first n triangle numbers
    
    Raises:
        ValueError: If n is less than 1
        TypeError: If input is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 1:
        raise ValueError("Number of triangle numbers must be at least 1")
    
    triangle_sequence = []
    for i in range(1, n + 1):
        triangle_num = (i * (i + 1)) // 2
        triangle_sequence.append(triangle_num)
    
    return triangle_sequence