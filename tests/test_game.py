import pytest
from life.game import GameClass


@pytest.fixture
def output():
  return '\n'.join([
    ' . . . . .',
    ' . . . . .',
    ' . O O O .',
    ' . . . . .',
    ' . . . . .',
    '',
    ' . . . . .',
    ' . . O . .',
    ' . . O . .',
    ' . . O . .',
    ' . . . . .',
    '\n'
  ])


def test_run(output, capsys):
  iterations = 1
  starting_configuration_name = 'blinker'
  game = GameClass(starting_configuration_name)
  game.run(iterations=iterations)
  out, _ = capsys.readouterr()
  assert out == output, 'grid display failed'
