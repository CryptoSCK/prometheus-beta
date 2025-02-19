import pytest
from triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test generating a basic sequence of triangle numbers"""
    result = generate_triangle_sequence(5)
    assert result == [1, 3, 6, 10, 15]

def test_generate_triangle_sequence_single_number():
    """Test generating a single triangle number"""
    result = generate_triangle_sequence(1)
    assert result == [1]

def test_generate_triangle_sequence_invalid_input_zero():
    """Test that an error is raised when n is less than 1"""
    with pytest.raises(ValueError, match="Number of triangle numbers must be at least 1"):
        generate_triangle_sequence(0)

def test_generate_triangle_sequence_invalid_input_negative():
    """Test that an error is raised when n is negative"""
    with pytest.raises(ValueError, match="Number of triangle numbers must be at least 1"):
        generate_triangle_sequence(-5)

def test_generate_triangle_sequence_invalid_input_type():
    """Test that an error is raised when input is not an integer"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence("3")
        generate_triangle_sequence(3.14)
        generate_triangle_sequence(None)