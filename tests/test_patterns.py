import numpy
import pytest
from life.patterns import PatternsClass


@pytest.fixture()
def configuration():
  return {
    'rows': 5,
    'columns': 5,
    'starting_configuration': 'blinker',
    'delay': 1
  }


@pytest.fixture()
def test_grid():
  grid = numpy.zeros((5, 5), dtype=numpy.int)
  grid[2][1] = 1
  grid[2][2] = 1
  grid[2][3] = 1
  return grid


def test_set_configured_grid(configuration, test_grid):
  patterns = PatternsClass(configuration)
  patterns.set_configured_grid('blinker')
  assert numpy.array_equal(patterns.grid, test_grid), 'grid is not configured as expected'
