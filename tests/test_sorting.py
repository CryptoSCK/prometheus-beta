import pytest
from src.sorting import sort_nums, optimal_sort

def test_sort_nums():
    """
    Test the sort_nums function with known issues.
    This test demonstrates the intentional bug in the sorting implementation.
    """
    # Test case that exposes the bug in sort_nums
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = sort_nums(input_list)
    
    # The bug causes descending instead of ascending order
    assert result == [9, 6, 5, 4, 3, 2, 1, 1], "sort_nums should fail with an incorrect sorting"

def test_optimal_sort_standard():
    """
    Test the optimal_sort function with a standard input list.
    """
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = [1, 1, 2, 3, 4, 5, 6, 9]
    
    assert optimal_sort(input_list) == expected, "optimal_sort should correctly sort the list"

def test_optimal_sort_empty_list():
    """
    Test optimal_sort with an empty list.
    """
    assert optimal_sort([]) == [], "optimal_sort should handle empty list"

def test_optimal_sort_single_element():
    """
    Test optimal_sort with a single-element list.
    """
    assert optimal_sort([42]) == [42], "optimal_sort should handle single-element list"

def test_optimal_sort_negative_numbers():
    """
    Test optimal_sort with negative numbers.
    """
    input_list = [-3, -1, -4, 0, 5, 9, -2, 6]
    expected = [-4, -3, -2, -1, 0, 5, 6, 9]
    
    assert optimal_sort(input_list) == expected, "optimal_sort should handle negative numbers"

def test_optimal_sort_duplicate_numbers():
    """
    Test optimal_sort with duplicate numbers.
    """
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 6, 9]
    
    assert optimal_sort(input_list) == expected, "optimal_sort should handle duplicate numbers"