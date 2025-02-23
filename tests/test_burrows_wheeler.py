import pytest
from src.burrows_wheeler import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_basic():
    """Test basic functionality of BWT"""
    text = "BANANA"
    bwt, index = burrows_wheeler_transform(text)
    assert isinstance(bwt, str)
    assert isinstance(index, int)

def test_burrows_wheeler_transform_and_inverse():
    """Test that BWT and inverse BWT recover original text"""
    test_cases = [
        "BANANA",
        "hello world",
        "abracadabra",
        "mississippi",
        "A"
    ]
    
    for text in test_cases:
        # Perform forward transform
        bwt, index = burrows_wheeler_transform(text)
        
        # Perform inverse transform
        recovered_text = inverse_burrows_wheeler_transform(bwt, index)
        
        # Verify reconstruction
        assert recovered_text == text, f"Failed for text: {text}"

def test_burrows_wheeler_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-string input
    with pytest.raises(TypeError):
        burrows_wheeler_transform(123)
    
    # Test empty string
    with pytest.raises(ValueError):
        burrows_wheeler_transform("")

def test_inverse_burrows_wheeler_error_handling():
    """Test error handling for inverse BWT"""
    # Test non-string BWT input
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform(123, 0)
    
    # Test non-integer index
    with pytest.raises(TypeError):
        inverse_burrows_wheeler_transform("test", "0")
    
    # Test empty BWT string
    with pytest.raises(ValueError):
        inverse_burrows_wheeler_transform("", 0)
    
    # Test negative index
    with pytest.raises(ValueError):
        inverse_burrows_wheeler_transform("test", -1)

def test_edge_cases():
    """Test edge cases for BWT"""
    # Single character
    text = "A"
    bwt, index = burrows_wheeler_transform(text)
    recovered = inverse_burrows_wheeler_transform(bwt, index)
    assert recovered == text

    # Repeated characters
    text = "AAAA"
    bwt, index = burrows_wheeler_transform(text)
    recovered = inverse_burrows_wheeler_transform(bwt, index)
    assert recovered == text