# myapp.py
import logging
import mylib
from mylogger import logger as testlogger


def main():
    logger = testlogger(__name__)
    logger.info('Executing code')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()