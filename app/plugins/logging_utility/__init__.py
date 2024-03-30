import logging
import os
from logging.handlers import RotatingFileHandler

class LoggingUtility:
    @staticmethod
    def initialize_logging():
        """Initializes the application-wide logging configuration."""
        log_directory = "logs"
        log_filename = "application.log"
        max_log_size = 10 * 1024 * 1024  # 10 MB
        backup_count = 3  # Keep at most 3 log files

        # Ensure the log directory exists
        os.makedirs(log_directory, exist_ok=True)
        log_file_path = os.path.join(log_directory, log_filename)

        # Create a rotating file handler
        rotating_file_handler = RotatingFileHandler(
            log_file_path, maxBytes=max_log_size, backupCount=backup_count
        )

        # Set the log format
        log_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        rotating_file_handler.setFormatter(log_format)

        # Configure the root logger
        logging.basicConfig(level=logging.INFO, handlers=[rotating_file_handler])

        # Additional configuration to log messages to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_format)
        logging.getLogger().addHandler(console_handler)

        # Example of adding a log message upon successful configuration
        logging.info("Logging system initialized.")

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def debug(message):
        logging.debug(message)

    @staticmethod
    def critical(message):
        logging.critical(message)
