"""
Unit tests for the file_reader module.

This module tests the read_text_file function with various scenarios.
"""

import os
import pytest
from src.file_reader import read_text_file

def test_read_existing_text_file(tmp_path):
    """Test reading an existing text file."""
    test_file = tmp_path / "sample.txt"
    test_file.write_text("Hello, World!")
    
    content = read_text_file(str(test_file))
    assert content == "Hello, World!"

def test_read_empty_file(tmp_path):
    """Test reading an empty file."""
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    
    content = read_text_file(str(test_file))
    assert content == ""

def test_read_nonexistent_file():
    """Test reading a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("nonexistent_file.txt")

def test_read_file_with_unicode(tmp_path):
    """Test reading a file with unicode characters."""
    test_file = tmp_path / "unicode.txt"
    test_file.write_text("こんにちは世界")
    
    content = read_text_file(str(test_file))
    assert content == "こんにちは世界"