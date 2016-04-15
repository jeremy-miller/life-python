from os.path import dirname, join, realpath
from life.configuration import ConfigurationClass


def test_get_configuration():
  test_configuration = {
    'rows': 40,
    'columns': 40,
    'starting_configuration': 'gosper_glider_gun',
    'delay': 1
  }
  assert ConfigurationClass().get_configuration() == test_configuration, 'invalid configuration'


def test_get_invalid_configuration():
  test_configuration = {
    'rows': 40,
    'columns': 40,
    'starting_configuration': 'gosper_glider_gun',
    'delay': 1
  }
  config = ConfigurationClass()
  config._CONFIG_FILENAME = 'test_config.yml'
  config._config_filepath = join(dirname(realpath(__file__)), config._CONFIG_FILENAME)
  assert config.get_configuration() == test_configuration, 'invalid configuration'
