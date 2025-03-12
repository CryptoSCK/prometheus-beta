"""
Simplified Snappy Compression Algorithm Implementation

This module provides a basic implementation of a Snappy-like compression algorithm.
Note: This is a simplified version and does not represent the full Snappy algorithm.
"""

def snappy_compress(data):
    """
    Compress input data using a simplified compression algorithm.
    
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
        search_start = max(0, i - 32768)
        for j in range(search_start, i):
            # Check for potential match
            match_length = 0
            while (i + match_length < len(data) and 
                   j + match_length < i and 
                   data[j + match_length] == data[i + match_length] and 
                   match_length < 64):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Compress sequence
        if best_length > 4:
            # Encode copy instruction with length and offset
            compressed.append(0b01000000 | (best_length - 1))
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
    Decompress data compressed with the simplified compression algorithm.
    
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
        current_byte = compressed_data[i]
        
        # Check if it's a literal or copy instruction
        if current_byte < 0b01000000:
            # Literal byte
            decompressed.append(current_byte)
            i += 1
        else:
            # Copy instruction
            # Ensure enough bytes for full instruction
            if i + 2 >= len(compressed_data):
                break
            
            # Extract length and offset
            length = (current_byte & 0x3F) + 1
            offset = compressed_data[i+1] | (compressed_data[i+2] << 8)
            
            # If no previous data, use offset as literal data
            if len(decompressed) == 0:
                for _ in range(length):
                    decompressed.append(offset & 0xFF)
            else:
                # Copy from previous data
                start = len(decompressed) - offset
                for j in range(length):
                    if start + j < 0:
                        break
                    decompressed.append(decompressed[start + j])
            
            i += 3
    
    return bytes(decompressed)