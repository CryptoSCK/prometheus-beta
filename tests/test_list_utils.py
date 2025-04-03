import pytest
from src.list_utils import remove_unique_elements

def test_remove_unique_elements_basic():
    """Test removing unique elements from a list with duplicates."""
    assert sorted(remove_unique_elements([1, 2, 2, 3, 3, 4])) == [2, 3]

def test_remove_unique_elements_no_duplicates():
    """Test when no elements are repeated."""
    assert remove_unique_elements([1, 2, 3, 4]) == []

def test_remove_unique_elements_empty_list():
    """Test with an empty list."""
    assert remove_unique_elements([]) == []

def test_remove_unique_elements_all_duplicates():
    """Test with a list where all elements are duplicates."""
    assert sorted(remove_unique_elements([1, 1, 1, 1])) == [1]

def test_remove_unique_elements_multiple_occurrences():
    """Test with elements that appear more than twice."""
    assert sorted(remove_unique_elements([1, 1, 1, 2, 2, 2, 3])) == [1, 2]

def test_remove_unique_elements_mixed_counts():
    """Test with a mix of unique and duplicate elements."""
    assert sorted(remove_unique_elements([1, 1, 2, 2, 3, 4, 5, 5, 5])) == [1, 2, 5]