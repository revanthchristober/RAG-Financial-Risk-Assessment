# src/utils/logging_utils.py

import logging

def setup_logging():
    """Sets up logging for the application."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger
