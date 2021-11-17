import logging

def logger(name):
    file_formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    console_formatter = logging.Formatter('%(levelname)s :: %(message)s')

    file_handler = logging.FileHandler('logs/err.log')
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(file_formatter)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)

    log = logging.getLogger(name)
    log.addHandler(file_handler)
    log.addHandler(console_handler)
    log.setLevel(logging.DEBUG)

    return log