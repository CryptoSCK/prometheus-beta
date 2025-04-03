from typing import List, Tuple


def get_unique_pairs(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Returns all unique pairs of elements from a given list of integers.
    
    A unique pair is defined as a distinct combination of two elements, 
    where order does not matter. For example, (1, 2) and (2, 1) are considered 
    the same pair.
    
    Args:
        numbers (List[int]): A list of integers to find pairs from.
    
    Returns:
        List[Tuple[int, int]]: A list of unique pairs of integers.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> get_unique_pairs([1, 2, 3])
        [(1, 2), (1, 3), (2, 3)]
        >>> get_unique_pairs([])
        []
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Return empty list for lists with fewer than 2 elements
    if len(numbers) < 2:
        return []
    
    # Use set to ensure uniqueness and prevent duplicate pairs
    unique_pairs = set()
    
    # Generate pairs using nested loops
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Create pair with smaller element first to avoid duplicates
            pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
            unique_pairs.add(pair)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_pairs))