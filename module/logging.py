import logging


def log_error(msg):
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s :: %(levelname)s :: %(message)s', file='logs/err.txt')
    logging.error(msg)

