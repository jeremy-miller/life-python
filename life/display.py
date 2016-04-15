"""This module displays the Life 'grid'."""

import numpy


class DisplayClass(object):  # pylint: disable=R0903
  """This class displays the Life 'grid'.

  No OpenGL or Matplotlib UI is used since this program is being executed
  in a Docker container.  The 'curses' Python package is also not used
  since it also has problems detecting the terminal when executed in a
  Docker container.
  """
  @staticmethod
  def display(grid):
    """This function displays the Life 'grid' to the console.

    Each iteration of the game will display a new grid in the console.

    This function loops through each index in the grid, checking if
    each cell is 'living' or 'dead', and adding the appropriate symbol
    to the grid output.

    Args:
      grid (array): A Numpy two-dimensional array which is the 'grid' to be
        displayed in the console.
    """
    output = ''
    for index, value in numpy.ndenumerate(grid):  # example 'index' = (0,0), example 'value' = 1
      if value:
        output += ' O'
      else:
        output += ' .'
      if index[1] == grid.shape[1] - 1:  # check to see if we are at the end of a row
        output += '\n'
    print(output)
