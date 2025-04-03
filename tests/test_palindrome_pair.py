import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(11) == True
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(0) == True
    assert is_palindrome(10) == False

def test_palindrome_pair_positive_cases():
    """Test cases where palindrome pair exists."""
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # 4 - 2 = 2 (palindrome)
    assert palindrome_pair([10, 12, 22, 34]) == True  # 22 - 10 = 12 (palindrome)
    assert palindrome_pair([11, 22, 33, 44]) == True  # 44 - 33 = 11 (palindrome)

def test_palindrome_pair_negative_cases():
    """Test cases where no palindrome pair exists."""
    assert palindrome_pair([1, 3, 5, 7]) == False
    assert palindrome_pair([10, 20, 30, 40]) == False
    assert palindrome_pair([]) == False
    assert palindrome_pair([5]) == False

def test_palindrome_pair_edge_cases():
    """Test edge cases and boundary conditions."""
    assert palindrome_pair([0, 1, 2]) == True  # 1 - 0 = 1 (palindrome)
    assert palindrome_pair([-11, 0, 11]) == True  # 11 - 0 = 11 (palindrome)

def test_palindrome_pair_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        palindrome_pair("not a list")
    
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, 'a', 3])
    
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, None, 3])