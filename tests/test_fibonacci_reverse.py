import pytest
from src.fibonacci_reverse import fibonacci_reverse

def test_fibonacci_reverse_zero():
    """Test generating Fibonacci sequence for n=0."""
    assert fibonacci_reverse(0) == []

def test_fibonacci_reverse_one():
    """Test generating Fibonacci sequence for n=1."""
    assert fibonacci_reverse(1) == [0]

def test_fibonacci_reverse_two():
    """Test generating Fibonacci sequence for n=2."""
    assert fibonacci_reverse(2) == [1, 0]

def test_fibonacci_reverse_five():
    """Test generating Fibonacci sequence for n=5."""
    assert fibonacci_reverse(5) == [5, 3, 2, 1, 0]

def test_fibonacci_reverse_ten():
    """Test generating Fibonacci sequence for n=10."""
    expected = [55, 34, 21, 13, 8, 5, 3, 2, 1, 0]
    assert fibonacci_reverse(10) == expected

def test_fibonacci_reverse_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_reverse(-1)

def test_fibonacci_reverse_invalid_type():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(None)