from typing import Set, Union

def sum_perfect_squares_from_set(numbers: Set[int]) -> int:
    """
    Calculate the sum of all perfect squares that can be formed from the integers in the given set.
    
    Args:
        numbers (Set[int]): A set of integers to check for perfect square combinations.
    
    Returns:
        int: The sum of all unique perfect squares that can be formed from the input set.
    
    Raises:
        TypeError: If the input is not a set of integers.
        ValueError: If any number in the set is negative.
    
    Examples:
        >>> sum_perfect_squares_from_set({1, 2, 3})  # 1^2 + 2^2 = 1 + 4 = 5
        5
        >>> sum_perfect_squares_from_set({4, 9})  # 2^2 + 3^2 = 4 + 9 = 13
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
    
    # Find all unique perfect squares that can be formed
    unique_perfect_squares = set()
    
    # Check all possible combinations of numbers
    for num in numbers:
        # Check if the number itself is a perfect square
        root = int(num ** 0.5)
        if root * root == num:
            unique_perfect_squares.add(num)
        
        # Check combinations of numbers
        for other_num in numbers:
            combined_value = num * other_num
            root = int(combined_value ** 0.5)
            if root * root == combined_value:
                unique_perfect_squares.add(combined_value)
    
    # Return the sum of unique perfect squares
    return sum(unique_perfect_squares)