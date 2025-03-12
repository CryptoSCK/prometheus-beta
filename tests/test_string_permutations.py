import pytest
from src.string_permutations import generate_unique_permutations

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert generate_unique_permutations('') == []

def test_single_character():
    """Test a single character string."""
    assert generate_unique_permutations('a') == ['a']

def test_unique_characters():
    """Test a string with unique characters."""
    result = generate_unique_permutations('abc')
    expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    assert sorted(result) == sorted(expected)

def test_repeated_characters():
    """Test a string with repeated characters."""
    result = generate_unique_permutations('abb')
    expected = ['abb', 'bab', 'bba']
    assert sorted(result) == sorted(expected)

def test_invalid_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        generate_unique_permutations(123)
    
    with pytest.raises(TypeError):
        generate_unique_permutations(None)

def test_longer_string():
    """Test a longer string with multiple unique characters."""
    result = generate_unique_permutations('abcd')
    assert len(result) == 24  # 4! (4 factorial) unique permutations