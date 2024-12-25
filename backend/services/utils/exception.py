class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def handle_exception(exception, logger):
    logger.error(f"Exception occurred: {exception}")
    raise CustomException(f"Error: {exception}")
