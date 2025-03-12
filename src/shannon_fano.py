from collections import Counter
from typing import Dict, List, Union

def shannon_fano_encode(data: Union[str, List[str]]) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (Union[str, List[str]]): Input data to be encoded
    
    Returns:
        Dict[str, str]: Dictionary mapping original symbols to their Shannon-Fano codes
    
    Raises:
        ValueError: If input data is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to a list of characters if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Count frequency of each symbol
    freq_counter = Counter(data)
    
    # Sort symbols by frequency in descending order
    sorted_symbols = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize code dictionary
    codes = {}
    
    def _generate_codes(symbols: List[tuple], prefix: str = ''):
        """
        Recursive helper function to generate Shannon-Fano codes
        
        Args:
            symbols (List[tuple]): List of (symbol, frequency) tuples
            prefix (str, optional): Current code prefix. Defaults to ''.
        """
        # Base case: single symbol
        if len(symbols) <= 1:
            if symbols:
                codes[symbols[0][0]] = prefix or '0'
            return
        
        # Find the split point that minimizes the difference between two groups
        total_freq = sum(freq for _, freq in symbols)
        current_freq = 0
        split_index = 0
        min_diff = float('inf')
        
        for i in range(len(symbols)):
            current_freq += symbols[i][1]
            group_diff = abs(current_freq - (total_freq - current_freq))
            
            if group_diff < min_diff:
                min_diff = group_diff
                split_index = i
        
        # Recursively generate codes for each group
        _generate_codes(symbols[:split_index+1], prefix + '0')
        _generate_codes(symbols[split_index+1:], prefix + '1')
    
    # Generate codes
    _generate_codes(sorted_symbols)
    
    return codes

def shannon_fano_decode(encoded_data: Dict[str, str], encoded_message: str) -> str:
    """
    Decode a message encoded with Shannon-Fano coding.
    
    Args:
        encoded_data (Dict[str, str]): Code mapping from symbols to their codes
        encoded_message (str): Encoded binary message
    
    Returns:
        str: Decoded original message
    
    Raises:
        ValueError: If decoding is not possible
    """
    # Invert the encoding dictionary for decoding
    decode_map = {code: symbol for symbol, code in encoded_data.items()}
    
    # Decode the message
    decoded_message = []
    current_code = ''
    
    for bit in encoded_message:
        current_code += bit
        
        # Check if current code is in decode map
        if current_code in decode_map:
            decoded_message.append(decode_map[current_code])
            current_code = ''
    
    # Ensure full decoding
    if current_code:
        raise ValueError("Unable to fully decode the message")
    
    return ''.join(decoded_message)