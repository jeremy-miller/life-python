import logging
import numpy


class PatternsClass(object):
  def __init__(self, configuration):
    self.grid = numpy.zeros((configuration['rows'], configuration['columns']), dtype=numpy.int)

  def get_configured_grid(self, starting_configuration):
    if starting_configuration == 'blinker':
      return self._set_blinker()
    elif starting_configuration == 'glider':
      return self._set_glider()
    elif starting_configuration == 'r-pentomino':
      return self._set_r_pentomino()
    elif starting_configuration == 'toad':
      return self._set_toad()
    elif starting_configuration == 'pulsar':
      return self._set_pulsar()
    elif starting_configuration == 'pentadecathlon':
      return self._set_pentadecathlon()
    elif starting_configuration == 'lightweight_spaceship':
      return self._set_lightweight_spaceship()
    else:
      logging.error('Invalid starting configuration: %s', starting_configuration)
      exit(1)

  def _set_blinker(self):
    logging.debug('Setting initial grid configuration: blinker')
    self.grid[2][1] = 1
    self.grid[2][2] = 1
    self.grid[2][3] = 1

  def _set_glider(self):
    logging.debug('Setting initial grid configuration: glider')
    self.grid[1][2] = 1
    self.grid[2][3] = 1
    self.grid[3][1] = 1
    self.grid[3][2] = 1
    self.grid[3][3] = 1

  def _set_r_pentomino(self):
    logging.debug('Setting initial grid configuration: r-pentomino')
    self.grid[1][2] = 1
    self.grid[1][3] = 1
    self.grid[2][1] = 1
    self.grid[2][2] = 1
    self.grid[3][2] = 1

  def _set_toad(self):
    logging.debug('Setting initial grid configuration: toad')
    self.grid[1][2] = 1
    self.grid[1][3] = 1
    self.grid[1][4] = 1
    self.grid[2][1] = 1
    self.grid[2][2] = 1
    self.grid[2][3] = 1

  def _set_pulsar(self):
    logging.debug('Setting initial grid configuration: pulsar')
    self.grid[1][3] = 1
    self.grid[1][4] = 1
    self.grid[1][5] = 1
    self.grid[1][9] = 1
    self.grid[1][10] = 1
    self.grid[1][11] = 1
    self.grid[3][1] = 1
    self.grid[3][6] = 1
    self.grid[3][8] = 1
    self.grid[3][13] = 1
    self.grid[4][1] = 1
    self.grid[4][6] = 1
    self.grid[4][8] = 1
    self.grid[4][13] = 1
    self.grid[5][1] = 1
    self.grid[5][6] = 1
    self.grid[5][8] = 1
    self.grid[5][13] = 1
    self.grid[6][3] = 1
    self.grid[6][4] = 1
    self.grid[6][5] = 1
    self.grid[6][9] = 1
    self.grid[6][10] = 1
    self.grid[6][11] = 1
    self.grid[8][3] = 1
    self.grid[8][4] = 1
    self.grid[8][5] = 1
    self.grid[8][9] = 1
    self.grid[8][10] = 1
    self.grid[8][11] = 1
    self.grid[9][1] = 1
    self.grid[9][6] = 1
    self.grid[9][8] = 1
    self.grid[9][13] = 1
    self.grid[10][1] = 1
    self.grid[10][6] = 1
    self.grid[10][8] = 1
    self.grid[10][13] = 1
    self.grid[11][1] = 1
    self.grid[11][6] = 1
    self.grid[11][8] = 1
    self.grid[11][13] = 1
    self.grid[13][3] = 1
    self.grid[13][4] = 1
    self.grid[13][5] = 1
    self.grid[13][9] = 1
    self.grid[13][10] = 1
    self.grid[13][11] = 1

  def _set_pentadecathlon(self):
    self.grid[1][3] = 1
    self.grid[1][8] = 1
    self.grid[2][1] = 1
    self.grid[2][2] = 1
    self.grid[2][4] = 1
    self.grid[2][5] = 1
    self.grid[2][6] = 1
    self.grid[2][7] = 1
    self.grid[2][9] = 1
    self.grid[2][10] = 1
    self.grid[3][1] = 1
    self.grid[3][8] = 1

  def _set_lightweight_spaceship(self):
    self.grid[1][2] = 1
    self.grid[1][5] = 1
    self.grid[2][1] = 1
    self.grid[3][1] = 1
    self.grid[3][5] = 1
    self.grid[4][1] = 1
    self.grid[4][2] = 1
    self.grid[4][3] = 1
    self.grid[4][4] = 1
