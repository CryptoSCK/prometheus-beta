import pytest
from src.near_palindrome_finder import find_near_palindrome_pairs

def test_find_near_palindrome_pairs_basic():
    test_input = ['abc', 'cab', 'def', 'fed']
    result = find_near_palindrome_pairs(test_input)
    assert len(result) == 2
    assert (['abc', 'cab'] in result or ['cab', 'abc'] in result)
    assert (['def', 'fed'] in result or ['fed', 'def'] in result)

def test_find_near_palindrome_pairs_empty_list():
    result = find_near_palindrome_pairs([])
    assert result == []

def test_find_near_palindrome_pairs_no_matches():
    test_input = ['hello', 'world', 'python']
    result = find_near_palindrome_pairs(test_input)
    assert result == []

def test_find_near_palindrome_pairs_single_character():
    test_input = ['a', 'b', 'c']
    result = find_near_palindrome_pairs(test_input)
    assert result == []

def test_find_near_palindrome_pairs_mixed_complexity():
    test_input = ['abc', 'cab', 'xyz', 'aaa', 'def', 'fed']
    result = find_near_palindrome_pairs(test_input)
    assert len(result) > 0
    for pair in result:
        assert len(pair) == 2

def test_find_near_palindrome_pairs_repeated_strings():
    test_input = ['abc', 'cab', 'abc', 'cab']
    result = find_near_palindrome_pairs(test_input)
    # Allow some flexibility in repeated string handling
    assert len(result) >= 1
    assert any(['abc', 'cab'] == pair or ['cab', 'abc'] == pair for pair in result)