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

    # pylint: disable = no-value-for-parameter
    # manager = LabyrinthManager()

    # labyrinth = manager.add_labyrinth(4, 4)

    # manager.show_labyrinth(labyrinth.id)

    # pp = manager.play_movement(labyrinth.id,'Up')

    # manager.show_labyrinth_play(labyrinth.id)  # TODO: store player_current_pos after player has moved

    # p2 = manager.play_movement(labyrinth.id,'Left')

    # manager.play_movement(labyrinth.id, 'left')

    # manager.play_movement(labyrinth.id, 'right')
    # manager.player_moved = True
    # manager.show_labyrinth_play(labyrinth.id, 'Up')

    # manager.show_labyrinth_play(labyrinth.id)

 