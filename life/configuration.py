"""This module reads, parses, validates, and returns the Life configuration settings."""

import logging
from os.path import dirname, join, realpath
from yaml import load


class ConfigurationClass(object):  # pylint: disable=R0903
  """This class reads, parses, validates, and returns the Life configuration settings."""
  def __init__(self, config_filename='config.yml', config_filepath=None):
    """This method sets the configuration filename, filepath, and configuration.

    Args:
      config_filename (str): The name of the configuration file.  Default is 'config.yml'.
      config_filepath (str): The path to the configuration file.

    Attributes:
      _config_filename (str): The name of the configuration file.
      _config_filepath (str): The path to the configuration file.  If no path is provided by
        the user, the local directory is used.
      _configuration (dict): The settings loaded from the configuration file.
    """
    self._config_filename = config_filename
    self._config_filepath = config_filepath if config_filepath else join(dirname(realpath(__file__)), config_filename)
    self._set_configuration()

  def _set_configuration(self):
    """This method reads, parses, and validates the configuration settings."""
    self._configuration = self._parse_yaml()
    self._validate_configuration()

  def _parse_yaml(self):
    """This method parses the Life configuration file.

    This method loads and parses the YAML configuration file from the provided filepath.

    Returns:
      A dictionary containing the configuration file keys and values.  For example:

      {
        'rows': 40,
        'columns': 40,
        'starting_configuration': 'gosper_glider_gun',
        'delay': 1
      }
    """
    logging.info('Loading and parsing %s', self._config_filename)
    logging.debug('%s filepath: %s', self._config_filename, self._config_filepath)
    with open(self._config_filepath, 'r') as f:
      parsed_yaml = load(f)
    logging.debug('Parsed yaml values: %s', parsed_yaml)
    return parsed_yaml

  def _validate_configuration(self):
    """This method validates the configuration values."""
    logging.debug('Validating configuration')
    self._validate_settings_exist_type()
    self._validate_values()

  def _validate_settings_exist_type(self):
    """This method validates the settings existence and type.

    This method validates the expected keys exist in the configuration, as well as that the
    values of the settings are the expected type.  This method does not validate that the
    'starting_configuration' setting contains one of the expected strings, since this validation
    is done when the starting configuration of the grid is being set.

    Raises:
      AssertionError: A validation error occurred.
    """
    logging.debug('Validating settings existence and type')
    assert 'rows' in self._configuration, 'Missing "rows" setting'
    assert isinstance(self._configuration['rows'], int), '"rows" setting must be an integer'
    assert 'columns' in self._configuration, 'Missing "columns" setting'
    assert isinstance(self._configuration['columns'], int), '"columns" setting must be an integer'
    assert 'starting_configuration' in self._configuration, 'Missing "starting_configuration" setting'
    assert isinstance(self._configuration['starting_configuration'], str), '"starting_configuration" setting must be a string'
    assert 'delay' in self._configuration, 'Missing "delay" setting'
    assert isinstance(self._configuration['delay'], int), '"delay" setting must be an integer'

  def _validate_values(self):
    """This method validates the settings values.

      This method validates the values of the settings meet minimum values for proper game function.
      """
    logging.debug('Validating setting values')
    if self._configuration['rows'] < 40:
      logging.info('"rows" setting too small, resetting to 40')
      self._configuration['rows'] = 40
    if self._configuration['columns'] < 40:
      logging.info('"columns" setting too small, resetting to 40')
      self._configuration['columns'] = 40
    if self._configuration['delay'] < 1:
      logging.info('"delay" setting too small, resetting to 1')
      self._configuration['delay'] = 1

  def get_configuration(self):
    """This method returns the Life configuration."""
    return self._configuration
