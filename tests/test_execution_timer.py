import logging
import time
import pytest
import re
from src.execution_timer import log_execution_time

# Setup a test logger
class TestLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_execution_time_basic():
    # Create a test logger
    test_logger = TestLogger()
    
    # Define a test function
    @log_execution_time(logger=test_logger)
    def sample_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y
    
    # Call the function
    result = sample_function(3, 4)
    
    # Check the result
    assert result == 7
    
    # Check logging
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    assert log_type == 'info'
    assert 'sample_function' in log_message
    assert 'executed in' in log_message

def test_log_execution_time_with_exception():
    # Create a test logger
    test_logger = TestLogger()
    
    # Define a function that raises an exception
    @log_execution_time(logger=test_logger)
    def error_function():
        raise ValueError("Test error")
    
    # Check that the exception is re-raised
    with pytest.raises(ValueError, match="Test error"):
        error_function()
    
    # Check logging
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    assert log_type == 'error'
    assert 'error_function' in log_message
    assert 'Test error' in log_message

def test_log_execution_time_default_logger():
    # Test with default logger
    @log_execution_time()
    def simple_function():
        time.sleep(0.05)
        return 42
    
    # Call the function and check the return value
    result = simple_function()
    assert result == 42

def test_log_execution_time_precision():
    # Create a test logger
    test_logger = TestLogger()
    
    # Define a function with very short execution time
    @log_execution_time(logger=test_logger)
    def quick_function():
        return "done"
    
    # Call the function
    result = quick_function()
    
    # Check the result
    assert result == "done"
    
    # Check logging
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    assert log_type == 'info'
    
    # Use regex to extract the time
    time_match = re.search(r'executed in ([\d.]+) seconds', log_message)
    assert time_match, "Could not find execution time in log message"
    
    # Check precision of extracted time
    time_str = time_match.group(1)
    parts = time_str.split('.')
    assert len(parts[1]) <= 4  # 4 or fewer decimal places

def test_log_execution_time_preserves_metadata():
    # Test that function metadata is preserved
    @log_execution_time()
    def test_func():
        """This is a test function docstring"""
        pass
    
    assert test_func.__name__ == 'test_func'
    assert test_func.__doc__ == 'This is a test function docstring'