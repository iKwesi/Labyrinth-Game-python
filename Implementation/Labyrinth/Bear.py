import random

from Helpers.IPlayer import IPlayer
from Helpers.Direction import Direction

# from Implementation.Labyrinth.treasure import Treasure

# from Implementation.Labyrinth.labyrinth import Labyrinth
# from Implementation.Labyrinth.labyrinth_manager import LabyrinthManager

class Bear(IPlayer):

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.bite = 5


# TODO: how to store item in inventory

    def get_player_pos(self, move_direction = None):
        # if not self.has_moved:
        if move_direction == None:
            # self.player_curr_pos = self.labyrinth.entry_coor  # create bear current pos
            self.bear_curr_pos = self.labyrinth.generation_path[random.randint(1, self.labyrinth.num_rows)]
            if self.bear_curr_pos == self.labyrinth.player.player_curr_pos:
                self.bear_hit(self.labyrinth.player)
            return self.bear_curr_pos
        else:
             self.move(move_direction)
        # elif self.has_moved:
        # self.player_curr_pos = self.labyrinth.entry_coor
        # print(f'Player current pos: {self.player_curr_pos}')
        # return self.player_curr_pos

    def bear_hit(self, target):
        return target.damage(self.bite)

    def move(self, move_direction):

        curr_row, curr_col = self.bear_curr_pos

        if move_direction.name == Direction.up.name:
            if self.labyrinth.check_monolith(curr_row + 1, curr_col): # edit from here
                print('Monolith encountered -> Up')
            else:
                curr_row += 1
        elif move_direction.name == Direction.down.name:
            if self.labyrinth.check_monolith(curr_row - 1, curr_col):
                print('Monolith encountered -> Down')
            else:
                curr_row -= 1
        elif move_direction.name == Direction.right.name:
            if self.labyrinth.check_monolith(curr_row, curr_col + 1):
                print('Monolith encountered -> Right')
            else:
                curr_col+= 1
        elif move_direction.name == Direction.left.name:
            if self.labyrinth.check_monolith(curr_row, curr_col - 1):
                print('Monolith encountered -> Left')
            else:
                curr_col -= 1
        self.bear_curr_pos = curr_row,curr_col
        if self.bear_curr_pos == self.labyrinth.player.player_curr_pos:
            self.bear_hit(self.labyrinth.player)
            print(f'The bear bit you')
            dir = random.choice(list(Direction))
            self.labyrinth.player.player_curr_pos = self.labyrinth.player.move(dir.name)
            print(f'player moved {dir.name}')
        print(f'bear now at: {self.bear_curr_pos}')

        return self.bear_curr_pos
