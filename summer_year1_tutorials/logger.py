# logger.py
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import os

def create_logger():
    # Get current and parent directories
    current_directory = Path(__file__).resolve().parent
    parent_directory = current_directory.parent

    # Ensure logs folder exists
    log_dir = parent_directory / "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Create logger
    logger = logging.getLogger('Summer_logger')
    logger.setLevel(logging.DEBUG)  # Root logger level

    # Stream handler (INFO level)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    stream_handler.setFormatter(stream_formatter)

    # File handler (ERROR level, rotating)
    file_handler = RotatingFileHandler(
        log_dir / "Summer.log",
        maxBytes=500_000,  # 500 KB
        backupCount=2
    )
    file_handler.setLevel(logging.ERROR)
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    file_handler.setFormatter(file_formatter)

    # Add handlers
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger

# Instantiate the logger
logger = create_logger()