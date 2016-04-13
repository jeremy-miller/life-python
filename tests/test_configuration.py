from life.configuration import ConfigurationClass


def test_get_configuration(self):
  test_configuration = {
    'rows': 40,
    'columns': 40,
    'starting_configuration': 'gosper_glider_gun',
    'delay': 1
  }
  assert ConfigurationClass().get_configuration() == test_configuration, 'invalid configuration'
