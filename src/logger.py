import logging
from sys import stdout
from datetime import datetime

cur_logger = None
def get_logger(module = "gpt-lecture-notes"):
    global cur_logger
    if cur_logger:
        return cur_logger
    logging.basicConfig(format="%(asctime)s %(levelname)-2s %(filename)s:%(funcName)s %(message)s")
    logger = logging.getLogger(module)
    log_level = logging.DEBUG
    logger.setLevel(log_level)

    logFormatter = logging.Formatter(
        "%(asctime)s %(levelname)-8s %(filename)s:%(funcName)s %(message)s"
    )
    consoleHandler = logging.StreamHandler(stdout)
    consoleHandler.setFormatter(logFormatter)

    current_date = datetime.now().date()
    iso_date = current_date.isoformat()
    fileHandler = logging.FileHandler(filename=f"logs/gpt-lecture-notes-{iso_date}.log")
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(log_level)
    logger.addHandler(fileHandler)

    cur_logger = logger
    return logger
