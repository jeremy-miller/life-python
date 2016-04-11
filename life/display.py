from time import sleep


class DisplayClass(object):
  _DISPLAY_TIMEOUT = 1  # seconds

  def show(self, grid):
    output = ''
    for y, row in enumerate(grid):
      for x, _ in enumerate(row):
        if grid[y][x]:
          output += ' O'
        else:
          output += ' .'
      output += '\n'
    print(output)
    sleep(self._DISPLAY_TIMEOUT)
