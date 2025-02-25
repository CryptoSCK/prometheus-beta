from typing import Set
from math import sqrt

def sum_perfect_squares_from_set(numbers: Set[int]) -> int:
    """
    Calculate the sum of all perfect squares that can be formed from the integers in the given set.
    
    A perfect square can only be formed by squaring a number from the set.
    
    Args:
        numbers (Set[int]): A set of integers to check for perfect square formations.
    
    Returns:
        int: The sum of all unique perfect squares formed by squaring numbers from the set.
    
    Raises:
        TypeError: If the input is not a set of integers.
        ValueError: If any number in the set is negative.
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3})  # 1^2 = 1, 2^2 = 4
        5
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
    
    # Find perfect squares by squaring numbers in the set
    perfect_squares = {num * num for num in numbers}
    
    return sum(perfect_squares)