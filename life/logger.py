import logging
from sys import stdout


class LoggerClass(object):
  @staticmethod
  def create_logger(log_level=logging.INFO):
    logger = logging.getLogger('')
    logger.setLevel(log_level)
    log_formatter = logging.Formatter("%(asctime)s %(message)s", datefmt='[%d/%b/%Y %H:%M:%S]')
    console_handler = logging.StreamHandler(stdout)
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    return logger
