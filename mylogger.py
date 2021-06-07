# myapp.py
import logging
import os
from datetime import datetime

def logger(name):
    
    filename = 'myapp_' + datetime.now().strftime("%Y-%m-%d") + '.log'
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", filename)
    logging.basicConfig(filename=path, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,encoding='utf-8', level=logging.DEBUG)

    logging.info(f'Logging instance started with name {name}')
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    
    return logger