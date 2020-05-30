from Helpers.IPlayer import IPlayer
from Helpers.Direction import Direction

from Implementation.Labyrinth.treasure import Treasure

# from Implementation.Labyrinth.labyrinth import Labyrinth
# from Implementation.Labyrinth.labyrinth_manager import LabyrinthManager

class Player(IPlayer):

    def __init__(self, labyrinth):

        self.inventory = []
        self.labyrinth = labyrinth
        self.treasure_loc = self.labyrinth.treasure
        self.item = self.labyrinth.treasure_item
        self.live = 2
        self.is_dead = False
        # self.move_direction = None
        # self.player_curr_pos = ()
        # self.player_current_pos()
        # self.has_moved = False

    def get_item(self):
        self.inventory.append(self.item)
        # print(f'{self.item} item added to inventory')
        print(f'step executed, {self.item}')

    def get_player_pos(self, move_direction = None):
        # if not self.has_moved:
        if move_direction == None:
            self.player_curr_pos = self.labyrinth.entry_coor
            if self.player_curr_pos == self.treasure_loc[0]:
                self.get_item()
            elif self.player_curr_pos in self.labyrinth.wormhole:
                print(f'You fell into a wormhole')
            return self.player_curr_pos
        else:
             self.move(move_direction)

    def damage(self, bite):
        self.live = self.live - bite
        if self.live <= 0:
            print('You were killed...')
            self.is_dead = True
        else:
            print(f'You have {self.live} live(s) left')
        return self.is_dead

    # def check_live(self):
    #     if self.live <= 0:
    #         print('You were killed!!!')

    
    # def move_to_next_wormhole(self):
    #     worm_idx = (self.labyrinth.wormhole.index(self.player_curr_pos) + 1) % 5
    #     print(f'worm_idx: {worm_idx}')
    #     return self.labyrinth.place_wormhole()[worm_idx]
    #     # return self.location()[worm_idx]
             
    def move(self, move_direction):

        curr_row, curr_col = self.player_curr_pos

        if move_direction == Direction.up.name:
            if self.labyrinth.check_monolith(curr_row + 1, curr_col): # edit from here
                print('Monolith encountered -> Up')
            else:
                curr_row += 1
        elif move_direction == Direction.down.name:
            if self.labyrinth.check_monolith(curr_row - 1, curr_col):
                print('Monolith encountered -> Down')
            else:
                curr_row -= 1
        elif move_direction == Direction.right.name:
            if self.labyrinth.check_monolith(curr_row, curr_col + 1):
                print('Monolith encountered -> Right')
            else:
                curr_col+= 1
        elif move_direction == Direction.left.name:
            if self.labyrinth.check_monolith(curr_row, curr_col - 1):
                print('Monolith encountered -> Left')
            else:
                curr_col -= 1
        self.player_curr_pos = curr_row,curr_col
        if self.player_curr_pos == self.treasure_loc[0]:
            self.get_item()

        # elif self.player_curr_pos in self.labyrinth.place_wormhole():
        elif self.player_curr_pos in self.labyrinth.wormhole:
            print(f'You fell into a wormhole')
            # self.player_curr_pos = self.labyrinth.next_wormhole()

        print(f'Player now at: {self.player_curr_pos}')

        return self.player_curr_pos
