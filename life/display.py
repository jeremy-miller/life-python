import numpy
from time import sleep


class DisplayClass(object):
  def __init__(self, delay):
    self._delay = delay  # seconds

  def show(self, grid):
    output = ''
    for index, value in numpy.ndenumerate(grid):
      if value:
        output += ' O'
      else:
        output += ' .'
      if index[1] == grid.shape[1] - 1:
        output += '\n'
    print(output)
    sleep(self._delay)
