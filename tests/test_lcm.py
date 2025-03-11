import pytest
from src.lcm import find_lcm

def test_lcm_basic_numbers():
    """Test LCM of basic positive integers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_lcm_one_number_is_multiple():
    """Test when one number is a multiple of the other"""
    assert find_lcm(4, 8) == 8
    assert find_lcm(7, 35) == 35

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert find_lcm(5, 7) == 35
    assert find_lcm(11, 13) == 143

def test_lcm_same_number():
    """Test LCM when both inputs are the same"""
    assert find_lcm(5, 5) == 5
    assert find_lcm(100, 100) == 100

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        find_lcm(4.5, 6)
    with pytest.raises(TypeError):
        find_lcm("4", 6)
    
    # Test non-positive inputs
    with pytest.raises(ValueError):
        find_lcm(0, 6)
    with pytest.raises(ValueError):
        find_lcm(4, -6)
    with pytest.raises(ValueError):
        find_lcm(-4, -6)