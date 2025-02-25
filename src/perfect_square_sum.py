from typing import Set
from math import sqrt

def sum_perfect_squares_from_set(numbers: Set[int]) -> int:
    """
    Calculate the sum of all perfect squares that can be formed from the integers in the given set.
    
    A perfect square can only be formed directly from a single number in the set being squared
    or from a combination of two numbers multiplied (if the result is a perfect square).
    
    Args:
        numbers (Set[int]): A set of integers to check for perfect square combinations.
    
    Returns:
        int: The sum of all unique perfect squares that can be formed from the input set.
    
    Raises:
        TypeError: If the input is not a set of integers.
        ValueError: If any number in the set is negative.
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3})  # 1^2 = 1
        1
        >>> sum_perfect_squares_from_set({4, 9})  # 2^2 = 4, 3^2 = 9
        13
    """
    # Validate input type
    if not isinstance(numbers, set):
        raise TypeError("Input must be a set of integers")
    
    # Validate input contains only integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Check for negative numbers
    if any(num < 0 for num in numbers):
        raise ValueError("All numbers must be non-negative")
    
    # Find unique perfect squares
    unique_perfect_squares = set()
    
    # Check for perfect squares in the set
    for num in numbers:
        # Find if the number is a perfect square of any integer
        root = int(sqrt(num)) if num > 0 else 0
        if root * root == num:
            unique_perfect_squares.add(num)
        
        # Check all possible multiplications with other numbers that could form a perfect square
        for other_num in numbers:
            product = num * other_num
            root = int(sqrt(product))
            if root * root == product:
                unique_perfect_squares.add(product)
    
    # Return the sum of unique perfect squares
    return sum(unique_perfect_squares)