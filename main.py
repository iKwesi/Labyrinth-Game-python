from __future__ import absolute_import
import sys

sys.path.append('../')

from Implementation.Labyrinth.labyrinth_manager import LabyrinthManager
from Implementation.Labyrinth.labyrinth import Labyrinth
# from Implementation.Labyrinth.Player import Player
from Implementation.Game import Game

if __name__ == "__main__":

    game = Game()

    game.game_initialize()
    game.game_start()


 