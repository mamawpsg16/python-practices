# import logging
import my_lib


# Set up logging configuration
# logger = logging.getLogger("main.py")
# logger.setLevel(logging.DEBUG) # Set the base level handler's 

# MANUAL LOGGING  

# Console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)  # Set the console handler's level

# File handler
# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.INFO)  # Set the file handler's level

# Create a formatter
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for each handler
# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# Add handlers to the logger
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# Test logging
# logger.debug('This will appear in the console but not in the file', extra=d)
# logger.info('This will appear in both the console and the file')
# logger.error('Error messages will also appear in both places')

import logging
def basic_config_error_log():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format='[%(asctime)s:%(levelname)s] - %(name)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

def main():
    # print(f"logger.name = {logger.name}")
    # print(f"logger.level = {logger.level}")
    basic_config_error_log()

if __name__ == '__main__':
    main()