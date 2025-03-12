"""
Simplified Snappy Compression Algorithm Implementation

This module provides a basic implementation of a Snappy-like compression algorithm.
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
        for j in range(max(0, i - 32768), i):
            # Check for potential match
            match_length = 0
            
            # Adjust search to prevent out-of-bounds access
            max_match = min(64, len(data) - i, i - j)
            
            while (match_length < max_match and 
                   data[j + match_length] == data[i + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = i - j
        
        # Compress sequence
        if best_length > 4:
            # Encode copy instruction (using bit manipulation for encoding)
            copy_marker = 0b01000000 | (best_length - 1)
            compressed.append(copy_marker)
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
        # Check if it's a literal or copy instruction
        if compressed_data[i] < 0b01000000:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
        else:
            # Copy instruction
            # Ensure there are enough bytes for copy instruction
            if i + 2 >= len(compressed_data):
                raise ValueError("Incomplete compression data")
            
            # Decode length and offset
            length = (compressed_data[i] & 0x3F) + 1
            offset = compressed_data[i+1] | (compressed_data[i+2] << 8)
            
            # Validate offset and perform copy operation
            if len(decompressed) == 0:
                # For first copy instruction, add literal-like data
                for _ in range(length):
                    decompressed.append(offset & 0xFF)
            else:
                # Perform copy from previous data
                if offset == 0 or offset > len(decompressed):
                    raise ValueError("Invalid compression: offset out of bounds")
                
                for _ in range(length):
                    source_index = len(decompressed) - offset
                    decompressed.append(decompressed[source_index])
            
            i += 3
    
    return bytes(decompressed)