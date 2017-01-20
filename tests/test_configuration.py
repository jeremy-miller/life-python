from life.configuration import ConfigurationClass


def test_get_configuration():
  starting_configuration_name = 'gosper_glider_gun'
  test_configuration = {'rows': 15, 'columns': 38}
  assert ConfigurationClass(starting_configuration_name).get_configuration() == test_configuration, 'invalid configuration received'


def test_get_invalid_starting_configuration_name():
  starting_configuration_name = 'gosper_glider'
  test_configuration = {'rows': 15, 'columns': 38}
  config = ConfigurationClass(starting_configuration_name)
  assert config.get_configuration() == test_configuration, 'invalid starting configuration name test failed'
