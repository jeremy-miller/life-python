import numpy


class DisplayClass(object):
  @staticmethod
  def show(grid):
    output = ''
    for index, value in numpy.ndenumerate(grid):  # example index = (0,0), example value = 1
      if value:
        output += ' O'
      else:
        output += ' .'
      if index[1] == grid.shape[1] - 1:  # check to see if we are at the end of a row
        output += '\n'
    print(output)
