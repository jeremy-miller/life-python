from os.path import dirname, join, realpath
from life.configuration import ConfigurationClass


def test_get_configuration():
  test_configuration = {
    'rows': 40,
    'columns': 40,
    'starting_configuration': 'gosper_glider_gun',
    'delay': 1
  }
  assert ConfigurationClass().get_configuration() == test_configuration, 'invalid configuration received'


def test_get_invalid_configuration():
  test_configuration = {
    'rows': 40,
    'columns': 40,
    'starting_configuration': 'gosper_glider_gun',
    'delay': 1
  }
  config_filepath = join(dirname(realpath(__file__)), 'test_config.yml')
  config = ConfigurationClass(config_filename='test_config.yml', config_filepath=config_filepath)
  assert config.get_configuration() == test_configuration, 'invalid configuration test failed'
