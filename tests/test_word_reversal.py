import pytest
from src.word_reversal import reverse_words_in_string

def test_basic_word_reversal():
    """Test basic word reversal"""
    assert reverse_words_in_string("Hello World") == "olleH dlroW"

def test_mixed_case_preservation():
    """Test preservation of original capitalization"""
    assert reverse_words_in_string("Python Is Great") == "nohtyP sI taerG"

def test_punctuation_preservation():
    """Test preservation of punctuation"""
    assert reverse_words_in_string("Hello, World!") == "olleH, dlroW!"

def test_multiple_punctuation():
    """Test multiple punctuation marks"""
    assert reverse_words_in_string("Hello, how are you?") == "olleH, woh era ?uoy"

def test_empty_string():
    """Test empty string input"""
    assert reverse_words_in_string("") == ""

def test_single_word():
    """Test single word input"""
    assert reverse_words_in_string("Python") == "nohtyP"

def test_multiple_spaces():
    """Test multiple spaces between words"""
    assert reverse_words_in_string("  Hello   World  ") == "  olleH   dlroW  "

def test_numbers_and_special_chars():
    """Test input with numbers and special characters"""
    assert reverse_words_in_string("Hello123 World!@#") == "olleH123 dlroW!@#"

def test_none_input():
    """Test None input"""
    assert reverse_words_in_string(None) is None