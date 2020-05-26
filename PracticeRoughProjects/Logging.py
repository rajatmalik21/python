import logging

logging.basicConfig\
        (
            format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(message)s',datefmt='%d-%m-%Y %H:%M:%S',
            level=logging.DEBUG,
            filename='logs.txt'
        )
#logger = logging.getLogger('test_logger')
#logger = logging.getLogger(__name__)
logger = logging.getLogger('books')

logger.info('This will not show up')
logger.warning('This will')
logging.debug('This is a debug message')
logging.critical('A critical error occurred')


"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
