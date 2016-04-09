import logging
from os.path import dirname, join, realpath
from yaml import load


class ConfigurationClass(object):
  _CONFIG_FILENAME = 'config.yml'

  def __init__(self):
    self._set_configuration()

  def _set_configuration(self):
    self._configuration = self._parse_yaml()
    self._validate_configuration()

  def _parse_yaml(self):
    filepath = join(dirname(realpath(__file__)), self._CONFIG_FILENAME)
    logging.info('Loading and parsing {}'.format(self._CONFIG_FILENAME))
    logging.debug('{} filepath: {}'.format(self._CONFIG_FILENAME, filepath))
    with open(filepath, 'r') as f:
      parsed_yaml = load(f)
    logging.debug('Parsed yaml values: {}'.format(parsed_yaml))
    return parsed_yaml

  def _validate_configuration(self):
    logging.debug('Validating configuration')
    assert 'rows' in self._configuration, 'Missing "rows" setting'
    assert isinstance(self._configuration['rows'], int), '"rows" setting must be an integer'
    assert 'columns' in self._configuration, 'Missing "columns" setting'
    assert isinstance(self._configuration['columns'], int), '"columns" setting must be an integer'
    assert 'starting_configuration' in self._configuration, 'Missing "starting_configuration" setting'
    # checking whether the 'starting_configuration' setting is valid will happen in patterns.py
    if self._configuration['rows'] < 5:
      logging.info('"rows" setting too small - resetting to 5')
      self._configuration['rows'] = 5
    if self._configuration['columns'] < 5:
      logging.info('"columns" setting too small - resetting to 5')
      self._configuration['columns'] = 5

  def get_configuration(self):
    return self._configuration
