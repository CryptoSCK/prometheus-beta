import pytest
from src.two_sum import find_two_sum_indices

def test_basic_two_sum():
    """Test finding two indices that sum to target"""
    nums = [2, 7, 11, 15]
    target = 9
    assert find_two_sum_indices(nums, target) == [0, 1]

def test_multiple_solutions():
    """Verify first solution is returned when multiple exist"""
    nums = [3, 2, 4, 3]
    target = 6
    assert find_two_sum_indices(nums, target) == [0, 3]

def test_no_solution():
    """Verify empty list is returned when no solution exists"""
    nums = [1, 2, 3, 4]
    target = 10
    assert find_two_sum_indices(nums, target) == []

def test_same_value_solution():
    """Test case where same value can be used twice"""
    nums = [3, 3]
    target = 6
    assert find_two_sum_indices(nums, target) == [0, 1]

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum_indices(123, 10)

def test_invalid_target_type():
    """Test raising TypeError for non-integer target"""
    with pytest.raises(TypeError, match="Target must be an integer"):
        find_two_sum_indices([1, 2, 3], "10")

def test_invalid_list_contents():
    """Test raising ValueError for non-integer list elements"""
    with pytest.raises(ValueError, match="List must contain only integers"):
        find_two_sum_indices([1, "2", 3], 5)

def test_empty_list():
    """Test behavior with an empty list"""
    assert find_two_sum_indices([], 5) == []

def test_large_input():
    """Test with a larger input to ensure efficiency"""
    nums = list(range(1000)) + [500, 500]
    target = 1000
    assert find_two_sum_indices(nums, target) == [500, 1000]