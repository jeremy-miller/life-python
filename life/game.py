"""This module contains the Life game logic."""

import logging
from time import sleep
import numpy
from life.configuration import ConfigurationClass
from life.display import DisplayClass
from life.patterns import PatternsClass


class GameClass(object):  # pylint: disable=R0903
  """This class contains the Life game logic.

  This class implements the functionality necessary to play Conway's Game of Life.
  It creates the game board (the 'grid') with the user-defined dimensions and starting configuration,
  then runs iterations of the game, sleeping between iterations.
  It outputs the grid to the console after each iteration.

  The rules of Conway's Game of Life are as follows:
  1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  2. Any live cell with two or three live neighbours lives on to the next generation.
  3. Any live cell with more than three live neighbours dies, as if by over-population.
  4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

  A cell is considered dead if it has a value of 0.  A cell is considered alive if it has a value of 1.

  Attributes:
    _max_rows (int):    The number of rows in the grid.
    _max_columns (int): The number of columns in the grid.
    _grid (array):      A Numpy two-dimensional array used to play the game.
    _display (class):   Instance of the DisplayClass
  """
  def __init__(self, starting_configuration_name):
    """This method instantiates the variables and classes necessary to begin playing Life."""
    configuration = ConfigurationClass(starting_configuration_name).get_configuration()
    self._max_rows = configuration['rows']
    self._max_columns = configuration['columns']
    patterns = PatternsClass(configuration)
    patterns.set_configured_grid(starting_configuration_name)
    self._grid = patterns.grid
    self._display = DisplayClass()

  def run(self, iterations=None):
    """This method runs the game of Life.

    This method displays the initial grid configuration to the console,
    then begins running iterations of the game, displaying the current
    state of the grid after each iteration.  If not iterations are set,
    the game will continue to run until the user exits the program.
    This method sleeps for a set period of time between iterations
    (to allow the user sufficient time to see the grid changes).

    Args:
      iterations (int): The number of iterations to run.
    """
    self._display.display(self._grid)
    if iterations:
      logging.debug('Running only %s iterations', iterations)
      for _ in range(iterations):
        self._run_iteration()
    else:  # pragma: no cover
      logging.debug('Running infinite iterations')
      while True:
        self._run_iteration()

  def _run_iteration(self):
    """This method runs one iteration of the game of Life."""
    logging.debug('Running new iteration')
    self._apply_game_rules()
    self._display.display(self._grid)
    sleep(1)  # sleep for one second between iterations of the game

  def _apply_game_rules(self):
    """This method applies the game rules to the existing grid.

    This method creates a new grid during each iteration (to satisfy rule 2).
    Then for each cell in the old grid, it calculates the live neighbors and
    updates the new grid.
    """
    logging.debug('Applying game rules')
    new_grid = numpy.copy(self._grid)
    for row, column in numpy.ndindex(self._grid.shape):  # ndindex returns every (row, column) pair in the array
      live_neighbors = self._get_live_neighbors(row, column)
      new_grid = self._update_grid(live_neighbors, new_grid, row, column)
    self._grid = new_grid

  def _get_live_neighbors(self, row, column):
    """This method calculates the number of live neighbors for a give cell.

    This method uses Numpy's array slicing to 'slice' out 9 cells (the current cell and its 8 neighbors)
    and sum their 'living' values.  It then removes the current cell's value from the final sum, since
    we only want to find living neighbors.  It also takes boundaries into account.

    Args:
      row (int):    The row index value of the current cell.
      column (int): The column index value of the current cell.

    Returns:
      The number of living neighbors for this cell in this iteration of the grid.
    """
    logging.debug('Getting live neighbors')
    min_row = max(row - 1, 0)
    max_row = min(row + 2, self._max_rows)  # add 2 (instead of 1) because the numpy array slicing upper bound is exclusive
    min_column = max(column - 1, 0)
    max_column = min(column + 2, self._max_columns)  # add 2 (instead of 1) because the numpy array slicing upper bound is exclusive
    return numpy.sum(self._grid[min_row:max_row, min_column:max_column]) - self._grid[row][column]

  def _update_grid(self, live_neighbors, new_grid, row, column):
    """This method updates the grid based on the number of living neighbors of a cell.

    This method implements logic for rules 1, 3, and 4 of the game.

    Args:
      live_neighbors (int): The number of living neighbors for the cell located at (row, column) in the current grid.
      new_grid (array):     The new copy of the Numpy grid, which will be updated in this method.
      row (int):            The row index value of the current cell.
      column (int):         The column index value of the current cell.

    Returns:
      The new grid, updated with the latest living/dead state of the cell located at (row, column) in the old grid.
    """
    logging.debug('Updating grid')
    if self._grid[row][column]:
      if live_neighbors < 2 or live_neighbors > 3:  # rule 1 and 3
        new_grid[row][column] = 0
    elif live_neighbors == 3:  # rule 4
      new_grid[row][column] = 1
    return new_grid
