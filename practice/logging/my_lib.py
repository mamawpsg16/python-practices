# mylib.py
import logging
logger = logging.getLogger(__name__) # GOOD

def do_something():
    logger.info('Doing something')