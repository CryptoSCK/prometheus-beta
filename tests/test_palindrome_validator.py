import pytest
from src.palindrome_validator import is_palindrome

def test_standard_palindromes():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_punctuation():
    """Test palindromes with punctuation and spaces"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    """Test that function is case-insensitive"""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_and_single_char():
    """Test empty string and single character inputs"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_non_palindromes():
    """Test strings that are not palindromes"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_special_characters():
    """Test handling of special characters"""
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("A man, a plan, a car!") == False

def test_numeric_palindromes():
    """Test numeric palindromes"""
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False