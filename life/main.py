import logging
from sys import exit
from life.logger import LoggerClass


class LifeClass(object):
  def __init__(self):
    pass

  def main(self):
    height = 5
    width = 5
    grid = [[False for x in range(height)] for x in range(width)]
    grid = self.blinker(grid)
    self.run(grid, height, width)


  def blinker(self, grid):
    grid[2][1] = True
    grid[2][2] = True
    grid[2][3] = True
    return grid

  def run(self, grid, height, width):
    new_grid = self.rules(grid, height, width)
    self.run(new_grid, height, width)

  def rules(self, grid, height, width):
    new_grid = [[False for x in range(height)] for x in range(width)]
    for row in range(len(grid)-1):
      for column in range(len(grid[row])-1):
        live_neighbors = 0

        if row-1 >= 0 and column-1 >= 0 and grid[row-1][column-1]:
          live_neighbors += 1
        if row-1 >= 0 and column >= 0 and grid[row-1][column]:
          live_neighbors += 1
        if row-1 >= 0 and column+1 <= width and grid[row-1][column+1]:
          live_neighbors += 1
        if column-1 >= 0 and grid[row][column-1]:
          live_neighbors += 1
        if column+1 >= width and grid[row][column+1]:
          live_neighbors += 1
        if row+1 >= height and column-1 >= 0 and grid[row+1][column-1]:
          live_neighbors += 1
        if row+1 >= height and column >= 0 and grid[row+1][column]:
          live_neighbors += 1
        if row+1 >= height and column+1 >= width and grid[row+1][column+1]:
          live_neighbors += 1

        if grid[row][column] and live_neighbors < 2:
          new_grid[row][column] = False
        elif grid[row][column] and (live_neighbors == 2 or live_neighbors == 3):
          new_grid[row][column] = True
        elif grid[row][column] and live_neighbors > 3:
          new_grid[row][column] = False
        elif not grid[row][column] and live_neighbors == 3:
          new_grid[row][column] = True
        else:
          new_grid[row][column] = False
    return new_grid


# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by over-population.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")
    LifeClass().main()
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
