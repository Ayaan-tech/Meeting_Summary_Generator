import logging

# Central logging setup
def setup_logging():
    logger = logging.getLogger("MeetingSummarizer")
    logger.setLevel(logging.INFO)
    
    # File handler for logging to a file
    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setLevel(logging.INFO)

    # Console handler for live output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatting log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Initialize logger
logger = setup_logging()
