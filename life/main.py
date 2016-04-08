import logging
import numpy
from sys import exit
from life.logger import LoggerClass


class LifeClass(object):
  def __init__(self, size):
    self._size = size
    self._grid = numpy.zeros((self._size, self._size), dtype=numpy.int)

  def main(self):
    self.blinker()
    self.run()

  def blinker(self):
    self._grid[2][1] = 1
    self._grid[2][2] = 1
    self._grid[2][3] = 1

  def run(self):
    self.run_iteration()
    self.run()

  def sum_neighbors(self, row, column):
    # use numpy's array slicing to "slice" out 9 cells (current cell and its 8 neighbors) and sum their 'living' values
    # then remove the current cell's value from the final sum since we're only finding living neighbors
    # also make sure we take boundary conditions into account
    return numpy.sum(self._grid[max(row - 1, 0):min(row + 2, self._size), max(column - 1, 0):min(column + 2, self._size)]) - self._grid[row][column]

  def run_iteration(self):
    new_grid = numpy.copy(self._grid)  # rule 2
    for row, column in numpy.ndindex(self._grid.shape):  # ndindex returns every (row, column) pair in the array
      live_neighbors = self.sum_neighbors(row, column)
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
    LifeClass(5).main()
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
