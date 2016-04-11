from time import sleep


class DisplayClass(object):
  _DISPLAY_TIMEOUT = 1  # seconds

  def show(self, grid):
    output = ''
    for i, row in enumerate(grid):
      for j, _ in enumerate(row):
        if grid[i][j]:
          output += ' O'
        else:
          output += ' .'
      output += '\n'
    print(output)
    sleep(self._DISPLAY_TIMEOUT)
