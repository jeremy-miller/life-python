"""This module returns the Life configuration settings."""

import logging


class ConfigurationClass(object):  # pylint: disable=R0903
  """This class returns the Life configuration settings."""

  STARTING_CONFIGURATION_NAMES = ['blinker', 'glider', 'toad', 'pulsar', 'pentadecathlon', 'lightweight_spaceship', 'gosper_glider_gun']
  CONFIGURATIONS = {
    'blinker': {'rows': 5, 'columns': 5, 'live_cells': [(2, 1), (2, 2), (2, 3)]},
    'glider': {'rows': 10, 'columns': 10, 'live_cells': [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]},
    'toad': {'rows': 5, 'columns': 5, 'live_cells': [(1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)]},
    'pulsar': {'rows': 16, 'columns': 16, 'live_cells': [
      (1, 3), (1, 4), (1, 5), (1, 9), (1, 10), (1, 11), (3, 1), (3, 6), (3, 8), (3, 13),
      (4, 1), (4, 6), (4, 8), (4, 13), (5, 1), (5, 6), (5, 8), (5, 13), (6, 3), (6, 4),
      (6, 5), (6, 9), (6, 10), (6, 11), (8, 3), (8, 4), (8, 5), (8, 9), (8, 10), (8, 11),
      (9, 1), (9, 6), (9, 8), (9, 13), (10, 1), (10, 6), (10, 8), (10, 13), (11, 1),
      (11, 6), (11, 8), (11, 13), (13, 3), (13, 4), (13, 5), (13, 9), (13, 10), (13, 11)
    ]},
    'pentadecathlon': {'rows': 18, 'columns': 11, 'live_cells': [
      (4, 5), (5, 5), (6, 4), (6, 6), (7, 5), (8, 5), (9, 5), (10, 5), (11, 4), (11, 6), (12, 5), (13, 5)
    ]},
    'lightweight_spaceship': {'rows': 7, 'columns': 20, 'live_cells': [(1, 1), (1, 4), (2, 5), (3, 1), (3, 5), (4, 2), (4, 3), (4, 4), (4, 5)]},
    'gosper_glider_gun': {'rows': 15, 'columns': 38, 'live_cells': [
      (1, 25), (2, 23), (2, 25), (3, 13), (3, 14), (3, 21), (3, 22), (3, 35), (3, 36), (4, 12), (4, 16),
      (4, 21), (4, 22), (4, 35), (4, 36), (5, 1), (5, 2), (5, 11), (5, 17), (5, 21), (5, 22), (6, 1),
      (6, 2), (6, 11), (6, 15), (6, 17), (6, 18), (6, 23), (6, 25), (7, 11), (7, 17), (7, 25), (8, 12),
      (8, 16), (9, 13), (9, 14)
    ]}
  }

  def __init__(self, starting_configuration_name):
    """This method sets the configuration options based on a starting configuration name (chosen by user).

    Args:
      starting_configuration_name (str):  The name of the starting Life game configuration.

    Attributes:
      _starting_configuration_name (str): The starting configuration name chosen by the user.
      _configuration (dict):              The settings associated with the name of the starting Life game configuration.
    """
    self._starting_configuration_name = starting_configuration_name
    self._set_configuration()

  def _set_configuration(self):
    """This method sets the configuration settings based on the starting configuration name."""
    self._validate_starting_configuration_name()
    self._configuration = self.CONFIGURATIONS[self._starting_configuration_name]

  def _validate_starting_configuration_name(self):  # pylint: disable=C0103
    """This method validates the starting configuration name chosen by the user."""
    logging.debug('Validating starting_configuration_name')
    if self._starting_configuration_name not in self.STARTING_CONFIGURATION_NAMES:
      logging.info('Invalid "starting_configuration_name", defaulting to "gosper_glider_gun"')
      self._starting_configuration_name = 'gosper_glider_gun'

  def get_configuration(self):
    """This method returns the Life configuration."""
    return self._configuration
