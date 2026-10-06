import logging  # brings in the logging module for logging messages
import sys      # gives access to stdout and stderr streams

def get_logger(name: str) -> logging.Logger:
    """Create and return a logger with a consistent format"""
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  # Return the existing logger if it already has handlers

    logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG

    handler = logging.StreamHandler(sys.stdout)  # Create a stream handler that outputs to stdout
    handler.setLevel(logging.DEBUG)  # Set the handler's logging level to DEBUG

    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)-8s %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)  # Set the formatter for the handler
    logger.addHandler(handler)  # Add the handler to the logger

    return logger  # Return the configured logger
    