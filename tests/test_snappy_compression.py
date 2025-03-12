"""
Unit tests for Snappy compression implementation
"""

import pytest
import sys
import os

# Ensure src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import snappy_compress, snappy_decompress

def test_compress_decompress_simple():
    """Test basic compression and decompression"""
    original = b"hello world hello world"
    compressed = snappy_compress(original)
    assert compressed != original
    decompressed = snappy_decompress(compressed)
    assert decompressed == original

def test_compress_decompress_repeated_sequence():
    """Test compression of highly repetitive data"""
    original = b"abcabcabcabcabcabc" * 10
    compressed = snappy_compress(original)
    # Compression might not always be effective for this pattern
    decompressed = snappy_decompress(compressed)
    assert decompressed == original

def test_compress_decompress_binary_data():
    """Test compression of binary data"""
    original = bytes(range(256)) * 5
    compressed = snappy_compress(original)
    decompressed = snappy_decompress(compressed)
    assert decompressed == original

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        snappy_compress("not bytes")
    
    with pytest.raises(TypeError):
        snappy_decompress("not bytes")

def test_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        snappy_compress(b'')
    
    with pytest.raises(ValueError):
        snappy_decompress(b'')

def test_compress_small_data():
    """Test compression of very small data"""
    original = b"a"
    compressed = snappy_compress(original)
    decompressed = snappy_decompress(compressed)
    assert decompressed == original

def test_complex_compression():
    """Test compression of a more complex input"""
    original = b"This is a test of the Snappy compression algorithm. " * 20
    compressed = snappy_compress(original)
    decompressed = snappy_decompress(compressed)
    assert decompressed == original