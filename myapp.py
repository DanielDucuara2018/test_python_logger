# myapp.py
import logging
import mylib
from datetime import datetime
import os

def main():
    filename = 'myapp_' + datetime.now().strftime("%Y-%m-%d") + '.log'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", filename)
    logging.basicConfig(filename=path, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,encoding='utf-8', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()