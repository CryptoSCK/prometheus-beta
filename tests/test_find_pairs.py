import pytest
from src.find_pairs import find_pairs_with_sum

def test_basic_pairs():
    """Test finding pairs in a simple scenario."""
    arr = [1, 2, 3, 4, 5]
    target_sum = 7
    expected = [(2, 5), (3, 4)]
    assert sorted(find_pairs_with_sum(arr, target_sum)) == sorted(expected)

def test_no_pairs():
    """Test when no pairs sum to the target."""
    arr = [1, 2, 3, 4, 5]
    target_sum = 10
    assert find_pairs_with_sum(arr, target_sum) == []

def test_single_pair():
    """Test when only one pair sums to the target."""
    arr = [1, 2, 3, 4, 5]
    target_sum = 6
    expected = [(1, 5), (2, 4)]
    assert sorted(find_pairs_with_sum(arr, target_sum)) == sorted(expected)

def test_zero_sum():
    """Test summing to zero."""
    arr = [-1, 0, 1, 2, -2]
    target_sum = 0
    expected = [(-1, 1), (-2, 2)]
    assert sorted(find_pairs_with_sum(arr, target_sum)) == sorted(expected)

def test_invalid_input_type():
    """Test raising TypeError for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_pairs_with_sum("not a list", 10)
    
    with pytest.raises(TypeError, match="Target sum must be an integer"):
        find_pairs_with_sum([1, 2, 3], "not an int")

def test_duplicate_elements():
    """Test raising ValueError for duplicate elements."""
    with pytest.raises(ValueError, match="Input array must contain unique elements"):
        find_pairs_with_sum([1, 2, 2, 3], 5)