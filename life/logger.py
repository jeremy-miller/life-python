"""This module creates a logger for formatted console logging."""

import logging
from sys import stdout


class LoggerClass(object):
  """This class creates a logger for formatted console logging."""
  @staticmethod
  def create_logger(log_level=logging.INFO):
    """This function creates a logger for formatted console logging.

    Args:
      log_level (int): The level at which to log.  Default is INFO.

    Returns:
      The configured logger.
    """
    logger = logging.getLogger('')
    logger.setLevel(log_level)
    log_formatter = logging.Formatter("%(asctime)s %(message)s", datefmt='[%d/%b/%Y %H:%M:%S]')
    console_handler = logging.StreamHandler(stdout)
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    return logger
