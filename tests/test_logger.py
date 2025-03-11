import logging
import pytest
from src.logger import log_multiple_values

def test_log_multiple_values(caplog):
    """Test logging multiple values with default settings"""
    caplog.set_level(logging.INFO)
    log_multiple_values("Hello", 42, "World")
    assert "Hello 42 World" in caplog.text

def test_log_multiple_values_with_kwargs(caplog):
    """Test logging with keyword arguments"""
    caplog.set_level(logging.INFO)
    log_multiple_values("User", name="John", age=30)
    assert "User name=John age=30" in caplog.text

def test_log_multiple_values_with_custom_delimiter(caplog):
    """Test logging with custom delimiter"""
    caplog.set_level(logging.INFO)
    log_multiple_values("A", "B", "C", delimiter="-")
    assert "A-B-C" in caplog.text

def test_log_multiple_values_different_levels(caplog):
    """Test logging at different levels"""
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    for level in levels:
        caplog.clear()
        caplog.set_level(getattr(logging, level.upper()))
        log_multiple_values("Test", level=level)
        assert f"Test" in caplog.text

def test_invalid_logging_level():
    """Test raising ValueError for invalid logging level"""
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_multiple_values("Test", level="invalid_level")

def test_mixed_types_logging(caplog):
    """Test logging with mixed data types"""
    caplog.set_level(logging.INFO)
    log_multiple_values(1, "string", [1, 2, 3], {"key": "value"})
    assert "1 string [1, 2, 3] {'key': 'value'}" in caplog.text