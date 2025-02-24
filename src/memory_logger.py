import psutil
import logging
import os

def log_memory_usage(logger=None):
    """
    Log current memory usage statistics.

    Args:
        logger (logging.Logger, optional): Logger to use for reporting. 
                If None, creates a default logger.

    Returns:
        dict: A dictionary containing memory usage statistics
    """
    # Create a default logger if none is provided
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        # Create console handler if no handlers exist
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

    # Get memory information
    memory = psutil.virtual_memory()
    
    # Prepare memory statistics
    memory_stats = {
        'total': memory.total,
        'available': memory.available,
        'used': memory.used,
        'percent': memory.percent
    }

    # Log memory usage
    logger.info(f"Memory Usage Statistics: {memory_stats}")

    return memory_stats