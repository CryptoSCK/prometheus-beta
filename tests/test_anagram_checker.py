import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_case_insensitive():
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    assert is_anagram("astronomer", "moon starer") == True
    assert is_anagram("  listen  ", "silent") == True

def test_non_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_empty_strings():
    assert is_anagram("", "") == True

def test_different_lengths():
    assert is_anagram("short", "longer") == False

def test_same_letters_different_count():
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "aaa") == False

def test_unicode_characters():
    assert is_anagram("résumé", "summer") == True

def test_type_errors():
    with pytest.raises(TypeError):
        is_anagram(123, "test")
    with pytest.raises(TypeError):
        is_anagram("test", [1,2,3])
    with pytest.raises(TypeError):
        is_anagram(None, "test")