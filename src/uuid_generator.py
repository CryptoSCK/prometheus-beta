import uuid

def generate_uuid() -> str:
    """
    Generate a new Universally Unique Identifier (UUID).
    
    Returns:
        str: A string representation of a randomly generated UUID.
    
    Example:
        >>> uuid_value = generate_uuid()
        >>> len(uuid_value) == 36  # Standard UUID format
        True
    """
    return str(uuid.uuid4())