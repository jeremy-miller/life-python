import logging
from sys import exit
from life.logger import LoggerClass
from life.game import GameClass


class MainClass(object):
  def __init__(self, rows, columns):
    self._game = GameClass(rows, columns)

  def main(self):
    self._game.blinker()
    self._game.run()


if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")
    MainClass(5, 5).main()
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
