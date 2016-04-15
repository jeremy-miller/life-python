"""This module sets the initial grid configuration."""

import logging
import numpy


class PatternsClass(object):  # pylint: disable=R0903
  """This class sets the initial grid configuration.

  These starting configurations are based on those found on http://www.conwaylife.com/wiki/Main_Page.

  Attributes:
    grid (array): A Numpy two-dimensional array containing the initial configuration.
  """
  def __init__(self, configuration):
    """This method instantiates the grid and defines the starting configuration functions.

    The grid is initialized to a Numpy array of all zeroes, since that is the default 'dead' state.
    The config_functions dictionary contains all the valid starting_configuration names, along
    with the associated indices which must be marked as 'living' at the beginning of the game.

    Args:
      configuration (dict): The configuration information parsed from the local configuration file.
    """
    self.grid = numpy.zeros((configuration['rows'], configuration['columns']), dtype=numpy.int)
    self._config_functions = {
      'blinker': [(2, 1), (2, 2), (2, 3)],
      'glider': [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
      'r-pentomino': [(1, 2), (1, 3), (2, 1), (2, 2), (3, 2)],
      'toad': [(1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)],
      'pulsar': [
        (1, 3), (1, 4), (1, 5), (1, 9), (1, 10), (1, 11), (3, 1), (3, 6), (3, 8), (3, 13),
        (4, 1), (4, 6), (4, 8), (4, 13), (5, 1), (5, 6), (5, 8), (5, 13), (6, 3), (6, 4),
        (6, 5), (6, 9), (6, 10), (6, 11), (8, 3), (8, 4), (8, 5), (8, 9), (8, 10), (8, 11),
        (9, 1), (9, 6), (9, 8), (9, 13), (10, 1), (10, 6), (10, 8), (10, 13), (11, 1),
        (11, 6), (11, 8), (11, 13), (13, 3), (13, 4), (13, 5), (13, 9), (13, 10), (13, 11)
      ],
      'pentadecathlon': [
        (4, 5), (5, 5), (6, 4), (6, 6), (7, 5), (8, 5), (9, 5), (10, 5),(11, 4), (11, 6), (12, 5), (13, 5)
      ],
      'lightweight_spaceship': [(1, 1), (1, 4), (2, 5), (3, 1), (3, 5), (4, 2), (4, 3), (4, 4), (4, 5)],
      'gosper_glider_gun': [
        (1, 25), (2, 23), (2, 25), (3, 13), (3, 14), (3, 21), (3, 22), (3, 35), (3, 36), (4, 12), (4, 16),
        (4, 21), (4, 22), (4, 35), (4, 36), (5, 1), (5, 2), (5, 11), (5, 17), (5, 21), (5, 22), (6, 1),
        (6, 2), (6, 11), (6, 15), (6, 17), (6, 18), (6, 23), (6, 25), (7, 11), (7, 17), (7, 25), (8, 12),
        (8, 16), (9, 13), (9, 14)
      ]
    }

  def set_configured_grid(self, starting_configuration):
    """This method sets the starting 'live' cells in the 'dead' grid.

    If the 'starting_configuration' variable is a valid option, the corresponding
    indices are set to 'living' in the grid.  If the provided 'starting_configuration'
    variable is not a valid option, the game is ended.

    Args:
      starting_configuration (str): The starting configuration string.
    """
    logging.debug('Setting starting configuration for %s', starting_configuration)
    if starting_configuration in self._config_functions:
      for index in self._config_functions[starting_configuration]:
        self.grid[index[0]][index[1]] = 1
    else:
      logging.error('Invalid starting configuration: %s', starting_configuration)
      exit(1)
