import gzip
import os
from typing import Union

def decompress_gzip_file(input_path: str, output_path: Union[str, None] = None) -> str:
    """
    Decompress a gzip file to a specified output path.

    Args:
        input_path (str): Path to the input gzip file.
        output_path (str, optional): Path where the decompressed file will be saved. 
                                     If None, uses input path without .gz extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there are issues reading or writing files.
        ValueError: If the input file is not a gzip file.
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate input file is a gzip file
    if not input_path.endswith('.gz'):
        raise ValueError(f"Input file must be a .gz file: {input_path}")
    
    # Determine output path
    if output_path is None:
        output_path = input_path[:-3]  # Remove .gz extension
    
    try:
        # Open and read the gzip file
        with gzip.open(input_path, 'rb') as f_in:
            # Write to the output file
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())
        
        return output_path
    except Exception as e:
        raise IOError(f"Error decompressing file: {str(e)}")