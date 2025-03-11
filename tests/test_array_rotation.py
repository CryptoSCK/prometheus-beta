import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 2)
    assert result == [3, 4, 5, 1, 2]

def test_full_rotation():
    """Test rotation equal to array length"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 5)
    assert result == arr

def test_rotation_larger_than_length():
    """Test rotation larger than array length"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 7)
    assert result == [3, 4, 5, 1, 2]

def test_zero_rotation():
    """Test zero rotation"""
    arr = [1, 2, 3, 4, 5]
    result = rotate_array_left(arr, 0)
    assert result == arr

def test_empty_array():
    """Test rotation of empty array"""
    arr = []
    result = rotate_array_left(arr, 2)
    assert result == []

def test_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_invalid_rotation_type():
    """Test invalid rotation type"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test negative rotation amount"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)

def test_preserve_original_array():
    """Ensure original array is not modified"""
    arr = [1, 2, 3, 4, 5]
    rotate_array_left(arr, 2)
    assert arr == [1, 2, 3, 4, 5]  # Original array should remain unchanged