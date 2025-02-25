import pytest
from src.perfect_square_sum import sum_perfect_squares_from_set

def test_basic_perfect_squares():
    """Test basic set of integers with perfect squares."""
    assert sum_perfect_squares_from_set({1, 2, 3}) == 5  # 1 from 1 and 4 from 2
    print("1 and 4:", {1, 2, 3}, "Result:", sum_perfect_squares_from_set({1, 2, 3}))

def test_empty_set():
    """Test with an empty set."""
    assert sum_perfect_squares_from_set(set()) == 0

def test_no_perfect_squares():
    """Test a set with no perfect squares."""
    assert sum_perfect_squares_from_set({5, 7, 11}) == 0
    print("No squares:", {5, 7, 11}, "Result:", sum_perfect_squares_from_set({5, 7, 11}))

def test_multiple_perfect_squares():
    """Test a set with multiple perfect squares and combinations."""
    result = sum_perfect_squares_from_set({1, 2, 3, 4, 9})
    assert result == 19  # 1 + 4 + 9 + 5
    print("Multiple squares:", {1, 2, 3, 4, 9}, "Result:", result)

def test_repeated_squares():
    """Test a set with repeated perfect squares."""
    assert sum_perfect_squares_from_set({4, 4, 9}) == 13  # 4 + 9
    print("Repeated squares:", {4, 4, 9}, "Result:", sum_perfect_squares_from_set({4, 4, 9}))

def test_large_numbers():
    """Test with larger numbers that form perfect squares."""
    assert sum_perfect_squares_from_set({16, 25, 36}) == 77
    print("Large squares:", {16, 25, 36}, "Result:", sum_perfect_squares_from_set({16, 25, 36}))

def test_invalid_input_type():
    """Test that TypeError is raised for non-set input."""
    with pytest.raises(TypeError, match="Input must be a set of integers"):
        sum_perfect_squares_from_set([1, 2, 3])  # List instead of set

def test_non_integer_input():
    """Test that TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_perfect_squares_from_set({1, 2.5, 3})

def test_negative_numbers():
    """Test that ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="All numbers must be non-negative"):
        sum_perfect_squares_from_set({1, -2, 3})