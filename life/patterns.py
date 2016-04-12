"""This module sets the initial grid configuration."""

import logging
import numpy


class PatternsClass(object):  # pylint: disable=R0903
  """This class sets the initial grid configuration.

  These starting configurations are based on those found on http://www.conwaylife.com/wiki/Main_Page.

  Attributes:
    grid (array): The initial grid configuration.
  """
  def __init__(self, configuration):
    """This method instantiates the grid and defines the starting configuration functions.

    The grid is initialized to a Numpy array of all zeroes, since that is the default 'dead' state.

    Args:
      configuration (dict): The configuration information parsed from the local configuration file.
    """
    self.grid = numpy.zeros((configuration['rows'], configuration['columns']), dtype=numpy.int)
    self._config_functions = {
      'blinker': self._set_blinker,
      'glider': self._set_glider,
      'r-pentomino': self._set_r_pentomino,
      'toad': self._set_toad,
      'pulsar': self._set_pulsar,
      'pentadecathlon': self._set_pentadecathlon,
      'lightweight_spaceship': self._set_lightweight_spaceship,
      'gosper_glider_gun': self._set_gosper_glider_gun
    }

  def set_configured_grid(self, starting_configuration):
    """This method sets the starting 'live' cells in the 'dead' grid.

    If the provided 'starting_configuration' variable is not a valid option,
    the game is ended.  If the 'starting_configuration' variable is a valid option,
    the corresponding function is executed to initialize the grid with the correct
    starting configuration.

    Args:
      starting_configuration (str): The starting configuration string.
    """
    if starting_configuration in self._config_functions:
      self._config_functions[starting_configuration]()
    else:
      logging.error('Invalid starting configuration: %s', starting_configuration)
      exit(1)

  def _set_blinker(self):
    """This method sets the 'blinker' starting configuration"""
    logging.debug('Setting initial grid configuration: blinker')
    self.grid[2][1] = 1
    self.grid[2][2] = 1
    self.grid[2][3] = 1

  def _set_glider(self):
    """This method sets the 'glider' starting configuration"""
    logging.debug('Setting initial grid configuration: glider')
    self.grid[1][2] = 1
    self.grid[2][3] = 1
    self.grid[3][1] = 1
    self.grid[3][2] = 1
    self.grid[3][3] = 1

  def _set_r_pentomino(self):
    """This method sets the 'r-pentomino' starting configuration"""
    logging.debug('Setting initial grid configuration: r-pentomino')
    self.grid[1][2] = 1
    self.grid[1][3] = 1
    self.grid[2][1] = 1
    self.grid[2][2] = 1
    self.grid[3][2] = 1

  def _set_toad(self):
    """This method sets the 'toad' starting configuration"""
    logging.debug('Setting initial grid configuration: toad')
    self.grid[1][2] = 1
    self.grid[1][3] = 1
    self.grid[1][4] = 1
    self.grid[2][1] = 1
    self.grid[2][2] = 1
    self.grid[2][3] = 1

  def _set_pulsar(self):
    """This method sets the 'pulsar' starting configuration"""
    logging.debug('Setting initial grid configuration: pulsar')
    self.grid[1][3] = 1
    self.grid[1][4] = 1
    self.grid[1][5] = 1
    self.grid[1][9] = 1
    self.grid[1][10] = 1
    self.grid[1][11] = 1
    self.grid[3][1] = 1
    self.grid[3][6] = 1
    self.grid[3][8] = 1
    self.grid[3][13] = 1
    self.grid[4][1] = 1
    self.grid[4][6] = 1
    self.grid[4][8] = 1
    self.grid[4][13] = 1
    self.grid[5][1] = 1
    self.grid[5][6] = 1
    self.grid[5][8] = 1
    self.grid[5][13] = 1
    self.grid[6][3] = 1
    self.grid[6][4] = 1
    self.grid[6][5] = 1
    self.grid[6][9] = 1
    self.grid[6][10] = 1
    self.grid[6][11] = 1
    self.grid[8][3] = 1
    self.grid[8][4] = 1
    self.grid[8][5] = 1
    self.grid[8][9] = 1
    self.grid[8][10] = 1
    self.grid[8][11] = 1
    self.grid[9][1] = 1
    self.grid[9][6] = 1
    self.grid[9][8] = 1
    self.grid[9][13] = 1
    self.grid[10][1] = 1
    self.grid[10][6] = 1
    self.grid[10][8] = 1
    self.grid[10][13] = 1
    self.grid[11][1] = 1
    self.grid[11][6] = 1
    self.grid[11][8] = 1
    self.grid[11][13] = 1
    self.grid[13][3] = 1
    self.grid[13][4] = 1
    self.grid[13][5] = 1
    self.grid[13][9] = 1
    self.grid[13][10] = 1
    self.grid[13][11] = 1

  def _set_pentadecathlon(self):
    """This method sets the 'pentadecathlon' starting configuration"""
    logging.debug('Setting initial grid configuration: pentadecathlon')
    self.grid[4][5] = 1
    self.grid[5][5] = 1
    self.grid[6][4] = 1
    self.grid[6][6] = 1
    self.grid[7][5] = 1
    self.grid[8][5] = 1
    self.grid[9][5] = 1
    self.grid[10][5] = 1
    self.grid[11][4] = 1
    self.grid[11][6] = 1
    self.grid[12][5] = 1
    self.grid[13][5] = 1

  def _set_lightweight_spaceship(self):
    """This method sets the 'lightweight spaceship' starting configuration"""
    logging.debug('Setting initial grid configuration: lightweight_spaceship')
    self.grid[1][1] = 1
    self.grid[1][4] = 1
    self.grid[2][5] = 1
    self.grid[3][1] = 1
    self.grid[3][5] = 1
    self.grid[4][2] = 1
    self.grid[4][3] = 1
    self.grid[4][4] = 1
    self.grid[4][5] = 1

  def _set_gosper_glider_gun(self):
    """This method sets the 'Gosper glider gun' starting configuration"""
    logging.debug('Setting initial grid configuration: gosper_glider_gun')
    self.grid[1][25] = 1
    self.grid[2][23] = 1
    self.grid[2][25] = 1
    self.grid[3][13] = 1
    self.grid[3][14] = 1
    self.grid[3][21] = 1
    self.grid[3][22] = 1
    self.grid[3][35] = 1
    self.grid[3][36] = 1
    self.grid[4][12] = 1
    self.grid[4][16] = 1
    self.grid[4][21] = 1
    self.grid[4][22] = 1
    self.grid[4][35] = 1
    self.grid[4][36] = 1
    self.grid[5][1] = 1
    self.grid[5][2] = 1
    self.grid[5][11] = 1
    self.grid[5][17] = 1
    self.grid[5][21] = 1
    self.grid[5][22] = 1
    self.grid[6][1] = 1
    self.grid[6][2] = 1
    self.grid[6][11] = 1
    self.grid[6][15] = 1
    self.grid[6][17] = 1
    self.grid[6][18] = 1
    self.grid[6][23] = 1
    self.grid[6][25] = 1
    self.grid[7][11] = 1
    self.grid[7][17] = 1
    self.grid[7][25] = 1
    self.grid[8][12] = 1
    self.grid[8][16] = 1
    self.grid[9][13] = 1
    self.grid[9][14] = 1
