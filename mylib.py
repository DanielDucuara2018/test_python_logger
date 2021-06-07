# mylib.py
from mylogger import logger as testlogger

def do_something():
    
    logger = testlogger(__name__)
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')