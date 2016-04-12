#!/usr/bin/python

"""This module runs the Life game."""

import logging
from life.logger import LoggerClass
from life.game import GameClass


class MainClass(object):
  """This class runs the Life game."""
  def __init__(self):
    """This method initializes the Life game."""
    self._game = GameClass()

  def run(self):
    """This method begins running the Life game."""
    self._game.run()


if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")
    MainClass().run()
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
