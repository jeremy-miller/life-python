"""This module returns the Life configuration settings."""

import logging


class ConfigurationClass(object):  # pylint: disable=R0903
  """This class returns the Life configuration settings."""

  STARTING_CONFIGURATION_NAMES = ['blinker', 'glider', 'toad', 'pulsar', 'pentadecathlon', 'lightweight_spaceship', 'gosper_glider_gun']
  CONFIGURATIONS = {
    'blinker': {'rows': 5, 'columns': 5},
    'glider': {'rows': 10, 'columns': 10},
    'toad': {'rows': 5, 'columns': 5},
    'pulsar': {'rows': 16, 'columns': 16},
    'pentadecathlon': {'rows': 18, 'columns': 11},
    'lightweight_spaceship': {'rows': 7, 'columns': 20},
    'gosper_glider_gun': {'rows': 15, 'columns': 38}
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
