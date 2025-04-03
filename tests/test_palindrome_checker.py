import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False

def test_case_insensitive():
    """Test that palindrome check is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_special_characters():
    """Test palindromes with special characters and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("!@#$%^&*()") == True  # Only checks alphanumeric chars

def test_empty_and_single_char():
    """Test edge cases with empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])