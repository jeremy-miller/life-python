import logging
from life.logger import LoggerClass


def test_create_logger():
  assert type(LoggerClass().create_logger()) == logging.RootLogger, 'invalid logger created'
