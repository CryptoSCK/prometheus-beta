import pytest
from src.shannon_fano import shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_basic_encoding():
    # Basic test with a simple string
    data = "hello"
    codes = shannon_fano_encode(data)
    
    # Verify codes are unique
    assert len(set(codes.values())) == len(codes)
    
    # Verify all expected characters are in the codes
    assert set(codes.keys()) == set(data)

def test_shannon_fano_full_encode_decode():
    # Test full encoding and decoding process
    original = "hello world"
    codes = shannon_fano_encode(original)
    
    # Encode the original message
    encoded_message = ''.join(codes[char] for char in original)
    
    # Decode the message
    decoded = shannon_fano_decode(codes, encoded_message)
    
    assert decoded == original

def test_shannon_fano_empty_input():
    # Test empty input raises ValueError
    with pytest.raises(ValueError):
        shannon_fano_encode([])
    
    with pytest.raises(ValueError):
        shannon_fano_encode("")

def test_shannon_fano_single_character():
    # Test single character input
    data = "a"
    codes = shannon_fano_encode(data)
    
    assert len(codes) == 1
    assert list(codes.values())[0] == '0'

def test_shannon_fano_undecodable_message():
    # Test decoding an invalid message
    codes = shannon_fano_encode("hello")
    
    with pytest.raises(ValueError):
        shannon_fano_decode(codes, "10101010101")  # Invalid bit sequence

def test_shannon_fano_frequency_sensitivity():
    # Test that more frequent characters get shorter codes
    data = "aaabbbcccdddeeefff"
    codes = shannon_fano_encode(data)
    
    # More frequent 'a' should have a shorter code
    a_code = codes['a']
    less_frequent_code = codes['f']
    
    assert len(a_code) < len(less_frequent_code)

def test_shannon_fano_list_input():
    # Test list input
    data = ['a', 'b', 'a', 'c', 'b', 'a']
    codes = shannon_fano_encode(data)
    
    assert len(codes) == 3  # 3 unique characters
    assert set(codes.keys()) == {'a', 'b', 'c'}

def test_shannon_fano_decode_edge_cases():
    # Test decoding with various inputs
    data = "abracadabra"
    codes = shannon_fano_encode(data)
    
    # Encode the original message
    encoded_message = ''.join(codes[char] for char in data)
    
    # Decode the message
    decoded = shannon_fano_decode(codes, encoded_message)
    
    assert decoded == data