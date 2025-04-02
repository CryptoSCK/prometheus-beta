import pytest
from src.max_sum_subarray import maxSumSubarray

def test_basic_max_sum_subarray():
    """Test basic functionality of maxSumSubarray"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 3
    assert maxSumSubarray(arr, k) == 39  # 10 + 23 + 3 = 39

def test_max_sum_single_subarray():
    """Test when only one subarray is possible"""
    arr = [1, 2, 3, 4, 5]
    k = 3
    assert maxSumSubarray(arr, k) == 12  # 3 + 4 + 5 = 12

def test_max_sum_with_negative_numbers():
    """Test functionality with negative numbers"""
    arr = [-1, -2, 3, 4, -5, 6, 7, -8]
    k = 3
    assert maxSumSubarray(arr, k) == 17  # 6 + 7 + (-8) = 5, or 3 + 4 + (-5) = 2, but 6 + 7 + (-8) = 5

def test_error_k_too_large():
    """Test error when k is larger than array length"""
    arr = [1, 2, 3]
    k = 4
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the input array"):
        maxSumSubarray(arr, k)

def test_error_k_zero_or_negative():
    """Test error when k is zero or negative"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        maxSumSubarray(arr, k=0)
    with pytest.raises(ValueError, match="Subarray length k must be a positive integer"):
        maxSumSubarray(arr, k=-1)

def test_empty_array():
    """Test with an empty array"""
    arr = []
    with pytest.raises(ValueError, match="Subarray length k cannot be larger than the input array"):
        maxSumSubarray(arr, k=1)

def test_max_sum_small_array():
    """Test with a small array and small k"""
    arr = [5, 2, 1]
    k = 2
    assert maxSumSubarray(arr, k) == 7  # 5 + 2 = 7