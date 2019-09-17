# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:05:39 2018

@author: 10541
"""

from time import strftime
from logging import Formatter,FileHandler,StreamHandler,getLogger,DEBUG
from sys import stdout

def setup_custom_logger(application_name):
    log_file_name = strftime(application_name+"_%d_%m_%Y")+'.log'
    formatter = Formatter('[%(asctime)s]  {%(pathname)s:%(lineno)d} \
                            %(levelname)s - %(message)s','%m-%d %H:%M:%S')
    handler = FileHandler(log_file_name, mode='a')
    handler.setFormatter(formatter)
    screen_handler = StreamHandler(stream=stdout)
    screen_handler.setFormatter(formatter)
    logger = getLogger(application_name)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    logger.removeHandler
    return logger

logger = setup_custom_logger('sample')
logger.info('Sample Info')
logger.error('Sample Error')
logger.warn('Sample Warning')