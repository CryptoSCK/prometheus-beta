import pytest
from src.delete_duplicates import deleteDuplicates

def test_delete_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    assert deleteDuplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_delete_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert deleteDuplicates([]) == []

def test_delete_duplicates_all_same():
    """Test list with all identical elements"""
    assert deleteDuplicates([1, 1, 1, 1]) == [1]

def test_delete_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert deleteDuplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_delete_duplicates_order_preservation():
    """Test that the order of first occurrence is preserved"""
    assert deleteDuplicates([5, 2, 6, 2, 5, 1]) == [5, 2, 6, 1]

def test_delete_duplicates_mixed_types():
    """Test with different types of integers"""
    assert deleteDuplicates([10, -1, 0, 10, -1, 5]) == [10, -1, 0, 5]