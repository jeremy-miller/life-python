import numpy
import pytest
from life.display import DisplayClass


@pytest.fixture
def grid():
  grid = numpy.zeros((3, 3), dtype=numpy.int)
  grid[1][1] = 1
  return grid


def test_show(grid, capsys):
  DisplayClass().display(grid)
  out, _ = capsys.readouterr()
  assert out == ' . . .\n . O .\n . . .\n\n', 'grid display failed'
