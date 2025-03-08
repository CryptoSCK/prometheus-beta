import pytest
from src.word_char_reverser import reverse_words_and_chars

def test_basic_reverse():
    """Test basic word and character reversal."""
    assert reverse_words_and_chars("Hello World") == "dlroW olleH"
    assert reverse_words_and_chars("Python is awesome") == "emosewa si nohtyP"

def test_single_word():
    """Test reversal of a single word."""
    assert reverse_words_and_chars("Python") == "nohtyP"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words_and_chars("") == ""

def test_multiple_spaces():
    """Test handling of strings with multiple spaces."""
    assert reverse_words_and_chars("  Hello   World  ") == "dlroW olleH"

def test_special_characters():
    """Test reversal with special characters and punctuation."""
    assert reverse_words_and_chars("Hello, World!") == "!dlroW ,olleH"

def test_numbers_and_words():
    """Test reversal with numbers and words."""
    assert reverse_words_and_chars("123 abc 456") == "654 cba 321"