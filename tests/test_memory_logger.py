import pytest
import logging
import psutil
from src.memory_logger import log_memory_usage

class MockLogger:
    def __init__(self):
        self.logged_messages = []
    
    def info(self, message):
        self.logged_messages.append(message)

def test_log_memory_usage_returns_dict():
    """Test that the function returns a dictionary with expected keys"""
    result = log_memory_usage()
    
    # Check that result is a dictionary
    assert isinstance(result, dict)
    
    # Check for expected keys
    expected_keys = ['total', 'available', 'used', 'percent']
    for key in expected_keys:
        assert key in result

def test_log_memory_usage_with_custom_logger():
    """Test logging with a custom logger"""
    mock_logger = MockLogger()
    
    result = log_memory_usage(mock_logger)
    
    # Check that a message was logged
    assert len(mock_logger.logged_messages) > 0

def test_memory_usage_values():
    """Test that memory usage values are reasonable"""
    result = log_memory_usage()
    
    # Total memory should be positive
    assert result['total'] > 0
    
    # Percent should be between 0 and 100
    assert 0 <= result['percent'] <= 100
    
    # Used memory should not exceed total memory
    assert result['used'] <= result['total']
    
    # Available memory should not exceed total memory
    assert result['available'] <= result['total']

def test_logging_behavior():
    """Test logging behavior with default logger"""
    # Capture log messages
    logger = logging.getLogger()
    original_handlers = logger.handlers.copy()
    
    try:
        # Remove existing handlers to simplify log capture
        for handler in original_handlers:
            logger.removeHandler(handler)
        
        # Create a stream handler to capture logs
        import io
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger.addHandler(handler)
        
        # Call the function
        log_memory_usage()
        
        # Check that something was logged
        log_capture.seek(0)
        logged_content = log_capture.read()
        assert "Memory Usage Statistics" in logged_content
    
    finally:
        # Restore original handlers
        logger.handlers = original_handlers