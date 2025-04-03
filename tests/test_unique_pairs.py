import pytest
from src.unique_pairs import get_unique_pairs


def test_normal_case():
    """Test with a typical list of integers"""
    result = get_unique_pairs([1, 2, 3])
    assert result == [(1, 2), (1, 3), (2, 3)]


def test_empty_list():
    """Test with an empty list"""
    result = get_unique_pairs([])
    assert result == []


def test_single_element_list():
    """Test with a list containing only one element"""
    result = get_unique_pairs([1])
    assert result == []


def test_list_with_duplicates():
    """Test with a list containing duplicate elements"""
    result = get_unique_pairs([1, 1, 2, 2, 3])
    assert result == [(1, 2), (1, 3), (2, 3)]


def test_negative_numbers():
    """Test with negative numbers"""
    result = get_unique_pairs([-1, -2, 0, 1])
    assert result == [(-2, -1), (-2, 0), (-2, 1), (-1, 0), (-1, 1), (0, 1)]


def test_large_list():
    """Test with a larger list of unique elements"""
    large_list = list(range(10))
    result = get_unique_pairs(large_list)
    assert len(result) == len(large_list) * (len(large_list) - 1) // 2


def test_invalid_input():
    """Test with invalid input type"""
    with pytest.raises(TypeError):
        get_unique_pairs("not a list")
    with pytest.raises(TypeError):
        get_unique_pairs(123)
    with pytest.raises(TypeError):
        get_unique_pairs(None)