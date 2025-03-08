"""
Unit tests for string reversal methods.
"""

import pytest
from src.string_reversal import (
    reverse_string_manual, 
    reverse_string_builtin, 
    reverse_string_slice,
    reverse_string_split_join,
    reverse_string_recursive
)

# Test cases to be used across multiple reversal methods
TEST_CASES = [
    ("hello", "olleh"),
    ("python", "nohtyp"),
    ("", ""),
    ("a", "a"),
    ("racecar", "racecar"),  # Palindrome
    ("12345", "54321"),      # Numeric string
    (" trim ", " mirt ")     # String with spaces
]

# List of all reversal functions to test
REVERSAL_FUNCTIONS = [
    reverse_string_manual,
    reverse_string_builtin, 
    reverse_string_slice,
    reverse_string_split_join,
    reverse_string_recursive
]

@pytest.mark.parametrize("func", REVERSAL_FUNCTIONS)
@pytest.mark.parametrize("input_str,expected", TEST_CASES)
def test_string_reversal(func, input_str, expected):
    """
    Test all string reversal methods with various inputs.
    """
    assert func(input_str) == expected

@pytest.mark.parametrize("func", REVERSAL_FUNCTIONS)
def test_string_reversal_type_error(func):
    """
    Test that type errors are raised for non-string inputs.
    """
    with pytest.raises(TypeError, match="Input must be a string"):
        func(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        func(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        func(["list"])

def test_different_methods_equivalence():
    """
    Verify that all reversal methods produce the same result.
    """
    test_strings = ["hello", "python", "", "racecar", "12345"]
    
    for test_str in test_strings:
        results = [func(test_str) for func in REVERSAL_FUNCTIONS]
        assert len(set(results)) == 1, f"Inconsistent reversal for {test_str}"