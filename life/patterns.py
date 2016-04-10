import logging
import numpy


class PatternsClass(object):
  def __init__(self, configuration):
    self._grid = numpy.zeros((configuration['rows'], configuration['columns']), dtype=numpy.int)

  def get_configured_grid(self, starting_configuration):
    if starting_configuration == 'blinker':
      return self._set_blinker()
    elif starting_configuration == 'glider':
      return self._set_glider()
    elif starting_configuration == 'r-pentomino':
      return self._set_r_pentomino()
    else:
      logging.error('Invalid starting configuration: %s', starting_configuration)
      exit(1)

  def _set_blinker(self):
    logging.debug('Setting initial grid configuration: blinker')
    self._grid[2][1] = 1
    self._grid[2][2] = 1
    self._grid[2][3] = 1
    return self._grid

  def _set_glider(self):
    logging.debug('Setting initial grid configuration: glider')
    self._grid[1][2] = 1
    self._grid[2][3] = 1
    self._grid[3][1] = 1
    self._grid[3][2] = 1
    self._grid[3][3] = 1
    return self._grid

  def _set_r_pentomino(self):
    logging.debug('Setting initial grid configuration: r-pentomino')
    self._grid[1][2] = 1
    self._grid[1][3] = 1
    self._grid[2][1] = 1
    self._grid[2][2] = 1
    self._grid[3][2] = 1
    return self._grid
