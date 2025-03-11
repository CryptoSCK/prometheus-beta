import logging
from typing import Any

def log_multiple_values(*args: Any, level: str = 'info', delimiter: str = ' ', **kwargs) -> None:
    """
    Log multiple values in a single statement with flexible configuration.

    Args:
        *args: Positional arguments to be logged
        level: Logging level (debug, info, warning, error, critical)
        delimiter: String used to separate values in the log message
        **kwargs: Additional keyword arguments to be logged

    Raises:
        ValueError: If an invalid logging level is provided
    """
    # Configure logging if not already configured
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger(__name__)

    # Validate logging level
    level_map = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    if level not in level_map:
        raise ValueError(f"Invalid logging level: {level}. Must be one of {list(level_map.keys())}")

    # Convert all arguments to strings and join
    log_message_parts = []
    
    # Add positional args
    log_message_parts.extend(str(arg) for arg in args)
    
    # Add keyword args
    for key, value in kwargs.items():
        log_message_parts.append(f"{key}={value}")
    
    # Join the message parts
    log_message = delimiter.join(log_message_parts)
    
    # Log at the specified level
    level_map[level](log_message)