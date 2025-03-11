import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from cycle_sort import cycle_sort

def test_cycle_sort_normal_list():
    """Test cycle sort with a standard list of integers."""
    test_list = [5, 2, 9, 1, 7, 6, 3]
    assert cycle_sort(test_list) == [1, 2, 3, 5, 6, 7, 9]

def test_cycle_sort_empty_list():
    """Test cycle sort with an empty list."""
    assert cycle_sort([]) == []

def test_cycle_sort_single_element():
    """Test cycle sort with a single-element list."""
    assert cycle_sort([42]) == [42]

def test_cycle_sort_already_sorted():
    """Test cycle sort with an already sorted list."""
    test_list = [1, 2, 3, 4, 5]
    assert cycle_sort(test_list) == [1, 2, 3, 4, 5]

def test_cycle_sort_reverse_sorted():
    """Test cycle sort with a reverse-sorted list."""
    test_list = [5, 4, 3, 2, 1]
    assert cycle_sort(test_list) == [1, 2, 3, 4, 5]

def test_cycle_sort_with_duplicates():
    """Test cycle sort with duplicate elements."""
    test_list = [4, 2, 2, 8, 3, 3, 1]
    assert cycle_sort(test_list) == [1, 2, 2, 3, 3, 4, 8]

def test_cycle_sort_negative_numbers():
    """Test cycle sort with negative numbers."""
    test_list = [-5, 2, -9, 1, 7, -6, 3]
    assert cycle_sort(test_list) == [-9, -6, -5, 1, 2, 3, 7]

def test_cycle_sort_invalid_input_type():
    """Test that cycle sort raises TypeError for non-list inputs."""
    with pytest.raises(TypeError):
        cycle_sort("not a list")
    with pytest.raises(TypeError):
        cycle_sort(123)
    with pytest.raises(TypeError):
        cycle_sort(None)

def test_cycle_sort_is_in_place():
    """Test that the sorting happens in-place."""
    test_list = [5, 2, 9, 1, 7, 6, 3]
    original_id = id(test_list)
    sorted_list = cycle_sort(test_list)
    assert id(sorted_list) == original_id  # Same list object
    assert sorted_list == [1, 2, 3, 5, 6, 7, 9]  # Correctly sorted