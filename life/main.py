import logging
import numpy
from sys import exit
from life.logger import LoggerClass


class LifeClass(object):
  def __init__(self, size):
    self._size = size
    self._grid = self.generate_grid()

  def main(self):
    self.blinker()
    self.run()

  def generate_grid(self):
    return numpy.zeros((self._size, self._size), dtype=numpy.int)

  def blinker(self):
    self._grid[2][1] = 1
    self._grid[2][2] = 1
    self._grid[2][3] = 1

  def run(self):
    self._grid = self.run_iteration()
    self.run()

  def run_iteration(self):
    new_grid = self.generate_grid()
    for row in range(self._grid.shape[0]):
      for column in range(self._grid.shape[0]):
        live_neighbors = 0

        if row-1 >= 0 and column-1 >= 0 and self._grid[row-1][column-1]:
          live_neighbors += 1
        if row-1 >= 0 and column >= 0 and self._grid[row-1][column]:
          live_neighbors += 1
        if row-1 >= 0 and column+1 < self._grid.shape[0] and self._grid[row-1][column+1]:
          live_neighbors += 1
        if column-1 >= 0 and self._grid[row][column-1]:
          live_neighbors += 1
        if column+1 < self._grid.shape[0] and self._grid[row][column+1]:
          live_neighbors += 1
        if row+1 < self._grid.shape[0] and column-1 >= 0 and self._grid[row+1][column-1]:
          live_neighbors += 1
        if row+1 < self._grid.shape[0] and column >= 0 and self._grid[row+1][column]:
          live_neighbors += 1
        if row+1 < self._grid.shape[0] and column+1 < self._grid.shape[0] and self._grid[row+1][column+1]:
          live_neighbors += 1

        if self._grid[row][column] and live_neighbors < 2:
          new_grid[row][column] = 0
        elif self._grid[row][column] and (live_neighbors == 2 or live_neighbors == 3):
          new_grid[row][column] = 1
        elif self._grid[row][column] and live_neighbors > 3:
          new_grid[row][column] = 0
        elif not self._grid[row][column] and live_neighbors == 3:
          new_grid[row][column] = 1
        else:
          new_grid[row][column] = 0
    self._grid = new_grid

if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")
    LifeClass().main(5)
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
