import random

from Helpers.IGameObject import IGameObject
from Helpers.Direction import Direction

class River(IGameObject):
    def __init__(self, labyrinth):
        self.name = 'River'
        self.labyrinth = labyrinth

    def __str__(self):
        return self.name

    def location(self):
        river = []
        river_start = self.labyrinth.generation_path[random.randint(1, self.labyrinth.num_rows)]
        river.append(river_start)

        river_length = random.randint(2,self.labyrinth.num_rows - 1)

        curr_row, curr_col = river[0][0],river[0][1]

        for i in range(river_length):
            dir = random.choice(list(Direction))
            
            if (curr_row < 0 or curr_row >= self.labyrinth.num_rows) or (curr_col < 0 and curr_col >= self.labyrinth.num_cols):
                break
            else:
                if dir.name == Direction.up.name:
                        curr_row += 1
                        # river.append((curr_row,curr_col))
                elif dir.name == Direction.down.name:
                        curr_row -= 1
                        # river.append((curr_row, curr_col))
                elif dir.name == Direction.right.name:
                        curr_col+= 1
                        # river.append((curr_row, curr_col))
                elif dir.name == Direction.left.name:
                        curr_col -= 1
                        # river.append((curr_row, curr_col))
                
                if (curr_row,curr_col) not in river:
                    river.append((curr_row, curr_col))
                else:
                    break
                
                curr_row, curr_col = river[i+1][0],river[i+1][1]
            
            # if self.labyrinth.player.player_curr_pos in river:
            #     print(f'You fell into the river')

            #     self.labyrinth.player.player_curr_pos = self.labyrinth.player.move(dir.name)
            #     print(f'player moved in river')
            # print(f'bear now at: {self.bear_curr_pos}')
        print(f'river: {river}')
        return river
