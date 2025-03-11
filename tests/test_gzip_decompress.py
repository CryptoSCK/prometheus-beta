import os
import gzip
import pytest
import shutil
from src.gzip_decompress import decompress_gzip_file

def create_sample_gzip_file(content, filename):
    """Helper function to create a sample gzip file for testing."""
    with gzip.open(filename, 'wb') as f:
        f.write(content.encode())

def test_decompress_gzip_file_default_output():
    # Create a sample gzip file
    test_content = "Hello, world!"
    input_file = 'tests/test_sample.txt.gz'
    create_sample_gzip_file(test_content, input_file)
    
    try:
        # Decompress the file
        output_file = decompress_gzip_file(input_file)
        
        # Verify the output file
        assert os.path.exists(output_file)
        assert output_file == input_file[:-3]
        
        # Check file contents
        with open(output_file, 'r') as f:
            assert f.read() == test_content
    finally:
        # Clean up test files
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(input_file[:-3]):
            os.remove(input_file[:-3])

def test_decompress_gzip_file_custom_output():
    # Create a sample gzip file
    test_content = "Custom output test"
    input_file = 'tests/test_sample.txt.gz'
    output_file = 'tests/custom_output.txt'
    create_sample_gzip_file(test_content, input_file)
    
    try:
        # Decompress the file to a custom output path
        decompressed_file = decompress_gzip_file(input_file, output_file)
        
        # Verify the output file
        assert os.path.exists(decompressed_file)
        assert decompressed_file == output_file
        
        # Check file contents
        with open(decompressed_file, 'r') as f:
            assert f.read() == test_content
    finally:
        # Clean up test files
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(output_file):
            os.remove(output_file)

def test_decompress_nonexistent_file():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file('non_existent_file.gz')

def test_decompress_non_gzip_file():
    # Create a non-gzip file
    with open('tests/not_gzip.txt', 'w') as f:
        f.write('Not a gzip file')
    
    try:
        # Test that ValueError is raised for non-gzip file
        with pytest.raises(ValueError):
            decompress_gzip_file('tests/not_gzip.txt')
    finally:
        # Clean up
        if os.path.exists('tests/not_gzip.txt'):
            os.remove('tests/not_gzip.txt')

def test_decompress_large_file():
    # Create a larger gzip file
    test_content = "A" * 1_000_000  # 1 million characters
    input_file = 'tests/large_file.txt.gz'
    create_sample_gzip_file(test_content, input_file)
    
    try:
        # Decompress the file
        output_file = decompress_gzip_file(input_file)
        
        # Verify the output file
        assert os.path.exists(output_file)
        
        # Check file contents
        with open(output_file, 'r') as f:
            assert f.read() == test_content
    finally:
        # Clean up test files
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(input_file[:-3]):
            os.remove(input_file[:-3])