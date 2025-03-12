import pytest
from src.string_case_converter import to_alternating_path_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert to_alternating_path_case("Hello World") == "hello-World"
    assert to_alternating_path_case("python is AWESOME") == "python-Is-awesome"

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_path_case("hello") == "hello"
    assert to_alternating_path_case("WORLD") == "world"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert to_alternating_path_case("this is a test") == "this-Is-a-Test"
    assert to_alternating_path_case("CONVERT multiple WORDS") == "convert-Multiple-words"

def test_numbers_and_special_chars():
    """Test handling of numbers and special characters."""
    assert to_alternating_path_case("123 test") == "123-Test"
    assert to_alternating_path_case("hello@world") == "helloworld"
    assert to_alternating_path_case("test 123 case") == "test-123-Case"

def test_empty_string():
    """Test empty string input."""
    assert to_alternating_path_case("") == ""

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_alternating_path_case(None)
    
    with pytest.raises(TypeError):
        to_alternating_path_case(123)

def test_whitespace_handling():
    """Test handling of extra whitespace."""
    assert to_alternating_path_case("  hello   world  ") == "hello-World"
    assert to_alternating_path_case(" multiple   SPACED words ") == "multiple-Spaced-words"