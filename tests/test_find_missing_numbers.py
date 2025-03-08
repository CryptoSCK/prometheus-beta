import pytest
from src.find_missing_numbers import find_missing_numbers

def test_basic_missing_numbers():
    """Test finding missing numbers in a typical scenario"""
    arr = [1, 2, 4, 6, 3, 7, 8]
    assert find_missing_numbers(arr) == [5]

def test_no_missing_numbers():
    """Test when no numbers are missing"""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_multiple_missing_numbers():
    """Test finding multiple missing numbers"""
    arr = [1, 2, 4, 7, 11, 12]
    assert find_missing_numbers(arr) == [3, 5, 6, 8, 9, 10]

def test_negative_numbers():
    """Test with negative numbers"""
    arr = [-3, -1, 0, 2, 4]
    assert find_missing_numbers(arr) == [-2, 1, 3]

def test_invalid_input_not_list():
    """Test that a non-list input raises ValueError"""
    with pytest.raises(ValueError, match="Input must be a list"):
        find_missing_numbers("not a list")

def test_empty_list():
    """Test that an empty list raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_numbers([])

def test_non_integer_input():
    """Test that non-integer inputs raise TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_numbers([1, 2, "3", 4])

def test_single_element_list():
    """Test a list with a single element"""
    arr = [5]
    assert find_missing_numbers(arr) == []