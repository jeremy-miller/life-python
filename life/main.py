#!/usr/bin/python

"""This module runs the Life game."""

import logging
from life.logger import LoggerClass
from life.game import GameClass


class MainClass(object):  # pylint: disable=R0903
  """This class runs the Life game."""
  def __init__(self):
    """This method initializes the Life game.

    Attributes:
      _starting_configuration_name (str): The starting configuration name chosen by the user
                                          Options are: 'blinker', 'glider', 'toad', 'pulsar', 'pentadecathlon', 'lightweight_spaceship', 'gosper_glider_gun'
      _game (GameClass):                  Instance of the Life game.
    """
    starting_configuration_name = 'blinker'
    self._game = GameClass(starting_configuration_name)

  def run(self):
    """This method begins running the Life game."""
    self._game.run(iterations=5)


if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")
    MainClass().run()
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
