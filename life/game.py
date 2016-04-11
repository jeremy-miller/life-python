import logging
import numpy
from life.configuration import ConfigurationClass
from life.display import DisplayClass
from life.patterns import PatternsClass


class GameClass(object):
  def __init__(self):
    configuration = ConfigurationClass().get_configuration()
    self._max_rows = configuration['rows']
    self._max_columns = configuration['columns']
    self._grid = PatternsClass(configuration).get_configured_grid(configuration['starting_configuration']).grid
    self._display = DisplayClass()

  def run(self):
    while True:
      self._run_iteration()
      self._display.show(self._grid)

  def _run_iteration(self):
    logging.debug('Running new iteration')
    new_grid = numpy.copy(self._grid)  # rule 2
    for row, column in numpy.ndindex(self._grid.shape):  # ndindex returns every (row, column) pair in the array
      live_neighbors = self._get_live_neighbors(row, column)
      new_grid = self._update_grid(live_neighbors, new_grid, row, column)
    self._grid = new_grid

  def _get_live_neighbors(self, row, column):
    logging.debug('Getting live neighbors')
    # use numpy's array slicing to "slice" out 9 cells (current cell and its 8 neighbors) and sum their 'living' values
    # then remove the current cell's value from the final sum since we're only finding living neighbors
    # also make sure we take boundary conditions into account
    min_row = max(row - 1, 0)
    max_row = min(row + 2,
                  self._max_rows)  # add 2 (instead of 1) because the numpy array slicing upper bound is exclusive
    min_column = max(column - 1, 0)
    max_column = min(column + 2,
                     self._max_columns)  # add 2 (instead of 1) because the numpy array slicing upper bound is exclusive
    return numpy.sum(self._grid[min_row:max_row, min_column:max_column]) - self._grid[row][column]

  def _update_grid(self, live_neighbors, new_grid, row, column):
    logging.debug('Updating grid')
    if self._grid[row][column]:
      if live_neighbors < 2 or live_neighbors > 3:  # rule 1 and 3
        new_grid[row][column] = 0
    elif live_neighbors == 3:  # rule 4
      new_grid[row][column] = 1
    return new_grid
