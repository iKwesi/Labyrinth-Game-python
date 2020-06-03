import itertools
import random

from Helpers.IGameObject import IGameObject

# from Implementation.Labyrinth.labyrinth import Labyrinth

class Wormhole(IGameObject):
    def __init__(self, labyrinth):
        self.name = 'Wormhole'
        self.labyrinth = labyrinth
    
    def __str__(self):
        return self.name

    # def move_to_next_wormhole(self):
    #     worm_idx = (self.labyrinth.wormhole.index(self.labyrinth.player.player_curr_pos) + 1) % 5
    #     print(f'worm_idx: {worm_idx}')
    #     return self.location()[worm_idx]

    def location(self):
        holes = [i for i in itertools.product(range(self.labyrinth.num_rows), repeat=2) if i not in self.labyrinth.river]
        wormholes = random.sample(holes, 5)
        # treasure.append(self.labyrinth.generation_path[random.randint(1, self.labyrinth.num_rows)])
        print(f'wormholes location: {wormholes}')
        return wormholes
