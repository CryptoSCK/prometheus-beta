"""
Snappy Compression Algorithm Implementation

This module provides a basic implementation of the Snappy compression algorithm.
Snappy is a fast compression/decompression library developed by Google.

Note: This is a simplified implementation and does not cover all 
complexities of the full Snappy algorithm.
"""

def snappy_compress(data):
    """
    Compress input data using a simplified Snappy-like compression algorithm.
    
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
    i = 0
    
    while i < len(data):
        # Look for repeated sequences
        best_length = 1
        best_offset = 0
        
        # Search backwards for potential matches
        for j in range(max(0, i - 32768), i):
            # Check for potential match
            match_length = 0
            while (i + match_length < len(data) and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 64):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Compress sequence
        if best_length > 4:
            # Encoded copy instruction
            compressed.append(best_length - 1)
            compressed.append(best_offset & 0xFF)
            compressed.append((best_offset >> 8) & 0xFF)
            i += best_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    return bytes(compressed)

def snappy_decompress(compressed_data):
    """
    Decompress data compressed with the simplified Snappy-like algorithm.
    
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
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check for copy instruction or literal
        if compressed_data[i] < 64:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
        else:
            # Copy instruction
            length = (compressed_data[i] & 0x3F) + 1
            offset = compressed_data[i+1] | (compressed_data[i+2] << 8)
            
            # Validate offset
            if offset > len(decompressed):
                raise ValueError("Invalid compression: offset out of bounds")
            
            # Copy matched sequence
            for j in range(length):
                decompressed.append(decompressed[len(decompressed) - offset + j])
            
            i += 3
    
    return bytes(decompressed)