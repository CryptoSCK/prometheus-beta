import pytest
from src.consecutive_diff_reorder import reorder_list_with_consecutive_diff

def test_empty_list():
    assert reorder_list_with_consecutive_diff([]) == []

def test_single_element():
    assert reorder_list_with_consecutive_diff([5]) == [5]

def test_already_valid_list():
    assert reorder_list_with_consecutive_diff([1, 2, 3]) == [1, 2, 3]
    assert reorder_list_with_consecutive_diff([3, 2, 1]) == [3, 2, 1]

def test_reorderable_list():
    result = reorder_list_with_consecutive_diff([1, 5, 3, 2, 4])
    assert result is not None
    
    # Verify each consecutive difference is 0, 1, or -1
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1

def test_unreorderable_list():
    assert reorder_list_with_consecutive_diff([1, 10, 100]) is None

def test_complex_reordering():
    result = reorder_list_with_consecutive_diff([7, 3, 5, 4, 6])
    assert result is not None
    
    # Verify each consecutive difference is 0, 1, or -1
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1

def test_duplicate_elements():
    result = reorder_list_with_consecutive_diff([3, 3, 4, 5])
    assert result is not None
    
    # Verify each consecutive difference is 0, 1, or -1
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1

def test_negative_numbers():
    result = reorder_list_with_consecutive_diff([-1, -3, -2, 0, 1])
    assert result is not None
    
    # Verify each consecutive difference is 0, 1, or -1
    for i in range(1, len(result)):
        assert abs(result[i] - result[i-1]) <= 1