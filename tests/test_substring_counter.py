import pytest
from src.substring_counter import count_substring_occurrences

def test_normal_substring_occurrence():
    """Test basic substring counting"""
    assert count_substring_occurrences("hello hello world", "hello") == 2
    assert count_substring_occurrences("mississippi", "iss") == 2

def test_no_occurrences():
    """Test when substring is not in the string"""
    assert count_substring_occurrences("hello world", "xyz") == 0

def test_overlapping_occurrences():
    """Test overlapping substring occurrences"""
    assert count_substring_occurrences("aaaaa", "aa") == 4

def test_entire_string_match():
    """Test when substring is the entire string"""
    assert count_substring_occurrences("hello", "hello") == 1

def test_substring_longer_than_string():
    """Test when substring is longer than the main string"""
    assert count_substring_occurrences("hi", "hello") == 0

def test_empty_string_inputs():
    """Test edge cases with empty strings"""
    assert count_substring_occurrences("", "") == 0
    assert count_substring_occurrences("hello", "") == 0

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        count_substring_occurrences(123, "hello")
    with pytest.raises(TypeError):
        count_substring_occurrences("hello", 123)

def test_substring_at_start_and_end():
    """Test occurrences at the start and end of the string"""
    assert count_substring_occurrences("hellohellohello", "hello") == 3

def test_case_sensitivity():
    """Test case-sensitive matching"""
    assert count_substring_occurrences("Hello HELLO hello", "Hello") == 1