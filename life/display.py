"""This module displays the Life 'grid'."""

import numpy


class DisplayClass(object):  # pylint: disable=R0903
  """This class displays the Life 'grid'."""
  @staticmethod
  def show(grid):
    """This function displays the Life 'grid' to the console.

    This function loops through each index in the grid, checking if
    each cell is 'living' or not, and adding the appropriate symbol
    to the grid output.
    """
    output = ''
    for index, value in numpy.ndenumerate(grid):  # example index = (0,0), example value = 1
      if value:
        output += ' O'
      else:
        output += ' .'
      if index[1] == grid.shape[1] - 1:  # check to see if we are at the end of a row
        output += '\n'
    print(output)
