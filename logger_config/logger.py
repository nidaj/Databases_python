import logging

def get_logger():
    # custom logger
    logger = logging.getLogger(__name__)

    # create handler
    file_handler = logging.FileHandler('logfile.log')
    file_handler.setLevel(logging.INFO)

    # create formatter and add to handler
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    # Add handler to the logger
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    return logger

