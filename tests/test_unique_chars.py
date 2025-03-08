import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    """Test basic functionality of extracting unique characters"""
    assert extract_unique_chars("123456789") == "123456789"
    assert extract_unique_chars("1112223334445") == "12345"
    assert extract_unique_chars("000111222") == "012"

def test_extract_unique_chars_empty():
    """Test handling of empty string"""
    assert extract_unique_chars("") == ""

def test_extract_unique_chars_single_char():
    """Test single character input"""
    assert extract_unique_chars("5") == "5"

def test_extract_unique_chars_mixed_repeats():
    """Test mixed repeating characters"""
    assert extract_unique_chars("10293847561") == "1029384756"

def test_extract_unique_chars_invalid_input_type():
    """Test input type validation"""
    with pytest.raises(TypeError):
        extract_unique_chars(12345)
    with pytest.raises(TypeError):
        extract_unique_chars(None)

def test_extract_unique_chars_invalid_characters():
    """Test handling of non-numeric characters"""
    with pytest.raises(ValueError):
        extract_unique_chars("123a456")
    with pytest.raises(ValueError):
        extract_unique_chars("12 34")
    with pytest.raises(ValueError):
        extract_unique_chars("12.34")