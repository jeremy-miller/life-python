import logging
from sys import exit
from life.logger import LoggerClass


class LifeClass(object):
  def __init__(self):
    pass


if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")

  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
