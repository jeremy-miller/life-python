"""This module reads, parses, validates, and returns the Life configuration file."""

import logging
from os.path import dirname, join, realpath
from yaml import load


class ConfigurationClass(object):  # pylint: disable=R0903
  """This class reads, parses, validates, and returns the Life configuration file.

  Attributes:
    _CONFIG_FILENAME (string): The name of the configuration YAML file located in the local folder.
  """
  _CONFIG_FILENAME = 'config.yml'

  def __init__(self):
    """This method sets the class instance configuration variable."""
    self._set_configuration()

  def _set_configuration(self):
    """This method reads, parses, and validates the configuration file."""
    self._configuration = self._parse_yaml()
    self._validate_configuration()

  def _parse_yaml(self):
    """This method parses the Life configuration file.

    This method loads and parses the YAML configuration file from the local folder.
    The name of the configuration file is set in the class variable '_CONFIG_FILENAME'

    Returns:
      A dictionary containing the configuration file keys and values.  For example:

      {
        'rows': 40,
        'columns': 40,
        'starting_configuration': 'gosper_glider_gun',
        'delay': 1
      }
    """
    logging.info('Loading and parsing %s', self._CONFIG_FILENAME)
    filepath = join(dirname(realpath(__file__)), self._CONFIG_FILENAME)
    logging.debug('%s filepath: %s', self._CONFIG_FILENAME, filepath)
    with open(filepath, 'r') as f:
      parsed_yaml = load(f)
    logging.debug('Parsed yaml values: %s', parsed_yaml)
    return parsed_yaml

  def _validate_configuration(self):
    """This method validates the configuration values.

    This method provides validation of the values within the class variable self._configuration.
    It validates that the expected keys are in the configuration dictionary, as well as
    that each value is the expected type.  It also verifies that certain settings have a minimum value.
    This method does not validate that the 'starting_configuration' setting contains one of the
    expected strings, since this validation is done within the 'patterns.py' file.
    """
    logging.debug('Validating configuration')
    self._validate_setting_existence_and_type()
    self._validate_values()

  def _validate_setting_existence_and_type(self):
    """This method validates the settings existence and type.

    This method validates the expected settings exist in the configuration, as well as that the
    values of the settings are the expected type.

    Raises:
      AssertionError: A validation error occurred.
    """
    logging.debug('Validating setting existence and type')
    assert 'rows' in self._configuration, 'Missing "rows" setting'
    assert isinstance(self._configuration['rows'], int), '"rows" setting must be an integer'
    assert 'columns' in self._configuration, 'Missing "columns" setting'
    assert isinstance(self._configuration['columns'], int), '"columns" setting must be an integer'
    assert 'starting_configuration' in self._configuration, 'Missing "starting_configuration" setting'
    assert 'delay' in self._configuration, 'Missing "delay" setting'
    assert isinstance(self._configuration['delay'], int), '"delay" setting must be an integer'

  def _validate_values(self):
    """This method validates the settings values.

      This method validates the values of the settings meet minimum values for proper game function.
      """
    logging.debug('Validating setting values')
    if self._configuration['rows'] < 40:
      logging.info('"rows" setting too small - resetting to 40')
      self._configuration['rows'] = 40
    if self._configuration['columns'] < 40:
      logging.info('"columns" setting too small - resetting to 40')
      self._configuration['columns'] = 40
    if self._configuration['delay'] < 1:
      logging.info('"delay" setting too small - resetting to 1')
      self._configuration['delay'] = 1

  def get_configuration(self):
    """This method returns the Life configuration."""
    return self._configuration
