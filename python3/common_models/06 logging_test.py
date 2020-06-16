import logging


logging.basicConfig(
    filename='06 logging.log',
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logging.warning('warning log.')
logging.critical('critical log.')
