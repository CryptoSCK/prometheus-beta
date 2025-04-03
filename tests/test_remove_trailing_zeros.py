import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros_basic():
    """Test removing trailing zeros from various numbers."""
    assert remove_trailing_zeros(10200) == 102
    assert remove_trailing_zeros(123) == 123
    assert remove_trailing_zeros(1000) == 1
    assert remove_trailing_zeros(0) == 0

def test_remove_trailing_zeros_edge_cases():
    """Test edge cases for trailing zero removal."""
    assert remove_trailing_zeros(10) == 1
    assert remove_trailing_zeros(100) == 1
    assert remove_trailing_zeros(1010) == 101

def test_remove_trailing_zeros_invalid_input():
    """Test error handling for invalid inputs."""
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        remove_trailing_zeros(-10)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        remove_trailing_zeros(10.5)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        remove_trailing_zeros("123")

def test_remove_trailing_zeros_large_number():
    """Test with a large number with multiple trailing zeros."""
    assert remove_trailing_zeros(1000000) == 1