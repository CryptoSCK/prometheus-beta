import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """Test that the generate_uuid function returns a valid UUID."""
    # Generate a UUID
    uuid_value = generate_uuid()
    
    # Check that the UUID is a string
    assert isinstance(uuid_value, str), "UUID should be a string"
    
    # Check UUID length (standard UUID format is 36 characters including hyphens)
    assert len(uuid_value) == 36, "UUID should be 36 characters long"
    
    # Validate UUID format using regex (version 4 UUID pattern)
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid_value, re.IGNORECASE), "UUID does not match expected format"

def test_uuid_uniqueness():
    """Test that multiple UUID generations produce unique values."""
    # Generate multiple UUIDs
    uuids = set(generate_uuid() for _ in range(1000))
    
    # Check that all generated UUIDs are unique
    assert len(uuids) == 1000, "Generated UUIDs should be unique"