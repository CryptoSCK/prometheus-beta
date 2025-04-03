import pytest
from src.one_char_deletion import can_convert_by_one_deletion

def test_basic_deletion_at_end():
    """Test deleting a character from the end of the string."""
    assert can_convert_by_one_deletion("abcd", "abc") == True

def test_basic_deletion_at_beginning():
    """Test deleting a character from the beginning of the string."""
    assert can_convert_by_one_deletion("abcd", "bcd") == True

def test_basic_deletion_in_middle():
    """Test deleting a character from the middle of the string."""
    assert can_convert_by_one_deletion("abcde", "abde") == True

def test_no_conversion_possible():
    """Test when no single character deletion can convert the string."""
    assert can_convert_by_one_deletion("abc", "def") == False

def test_different_length_impossible():
    """Test when the length difference is not exactly one."""
    assert can_convert_by_one_deletion("abc", "abcd") == False
    assert can_convert_by_one_deletion("abcd", "ab") == False

def test_empty_strings():
    """Test edge cases with empty strings."""
    assert can_convert_by_one_deletion("a", "") == True
    assert can_convert_by_one_deletion("", "a") == False

def test_single_character_strings():
    """Test conversion with single character strings."""
    assert can_convert_by_one_deletion("a", "") == True
    assert can_convert_by_one_deletion("", "a") == False

def test_identical_strings():
    """Test when strings are identical."""
    assert can_convert_by_one_deletion("abc", "abc") == False