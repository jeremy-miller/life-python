import logging
from life.logger import LoggerClass
from life.game import GameClass


class MainClass(object):
  def __init__(self):
    self._game = GameClass()

  def run(self):
    self._game.run()


if __name__ == '__main__':
  try:
    LoggerClass().create_logger()
    logging.info("Starting Conway's Game of Life...")
    MainClass().run()
  except KeyboardInterrupt:
    logging.info('Exiting...')
    exit()
