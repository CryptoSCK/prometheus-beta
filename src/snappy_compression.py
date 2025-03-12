"""
Basic Compression and Decompression Utility

This module provides simple compression and decompression functions.
Note: This is a very basic implementation and not a true Snappy algorithm.
"""

def snappy_compress(data):
    """
    Compress input data using a simple run-length encoding approach.
    
    Args:
        data (bytes): Input data to compress
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    compressed = bytearray()
    count = 1
    current = data[0]
    
    for byte in data[1:]:
        if byte == current and count < 255:
            count += 1
        else:
            # Store the count and the byte
            compressed.append(count)
            compressed.append(current)
            current = byte
            count = 1
    
    # Add the last sequence
    compressed.append(count)
    compressed.append(current)
    
    return bytes(compressed)

def snappy_decompress(compressed_data):
    """
    Decompress data compressed with the simple run-length encoding.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or appears to be corrupted
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Ensure even number of bytes
    if len(compressed_data) % 2 != 0:
        raise ValueError("Invalid compressed data")
    
    decompressed = bytearray()
    
    for i in range(0, len(compressed_data), 2):
        count = compressed_data[i]
        byte = compressed_data[i+1]
        
        # Repeat the byte 'count' times
        decompressed.extend([byte] * count)
    
    return bytes(decompressed)