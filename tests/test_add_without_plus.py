import pytest
from src.add_without_plus import add_without_plus

def test_basic_addition():
    """Test basic integer addition"""
    assert add_without_plus(3, 4) == 7
    assert add_without_plus(0, 0) == 0
    assert add_without_plus(10, 20) == 30

def test_negative_numbers():
    """Test addition with negative numbers"""
    assert add_without_plus(-5, 3) == -2
    assert add_without_plus(5, -3) == 2
    assert add_without_plus(-10, -5) == -15

def test_large_numbers():
    """Test addition with larger numbers"""
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(-1000, 1000) == 0

def test_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        add_without_plus('5', 3)
    
    with pytest.raises(TypeError):
        add_without_plus(5, '3')
    
    with pytest.raises(TypeError):
        add_without_plus([], 3)

def test_zero_additions():
    """Test addition with zero"""
    assert add_without_plus(0, 5) == 5
    assert add_without_plus(5, 0) == 5