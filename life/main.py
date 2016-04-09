import logging
import numpy
from sys import exit
from life.logger import LoggerClass


class LifeClass(object):
  def __init__(self, rows, columns):
    self._max_rows = rows
    self._max_columns = columns
    self._grid = numpy.zeros((self._max_rows, self._max_columns), dtype=numpy.int)

  def main(self):
    self.blinker()
    self.run()

  def blinker(self):
    self._grid[2][1] = 1
    self._grid[2][2] = 1
    self._grid[2][3] = 1

  def run(self):
    while True:
      self._run_iteration()

  def _sum_neighbors(self, row, column):
    # use numpy's array slicing to "slice" out 9 cells (current cell and its 8 neighbors) and sum their 'living' values
    # then remove the current cell's value from the final sum since we're only finding living neighbors
    # also make sure we take boundary conditions into account
    min_row = max(row - 1, 0)
    max_row = min(row + 2, self._max_rows)  # add 2 (instead of 1) because the numpy array slicing upper bound is exclusive
    min_column = max(column - 1, 0)
    max_column = min(column + 2, self._max_columns)  # add 2 (instead of 1) because the numpy array slicing upper bound is exclusive
    return numpy.sum(self._grid[min_row:max_row, min_column:max_column]) - self._grid[row][column]

  def _run_iteration(self):
    new_grid = numpy.copy(self._grid)  # rule 2
    for row, column in numpy.ndindex(self._grid.shape):  # ndindex returns every (row, column) pair in the array
      live_neighbors = self._sum_neighbors(row, column)
      if self._grid[row][column]:  # rule 1 and 3
        if live_neighbors < 2 or live_neighbors > 3:
          new_grid[row][column] = 0
      elif live_neighbors == 3:  # rule 4
        new_grid[row][column] = 1
    self._grid = new_grid


if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")
    LifeClass(5, 5).main()
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
