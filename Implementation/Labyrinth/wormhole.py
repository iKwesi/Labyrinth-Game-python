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

    def location(self):
        holes = [i for i in itertools.product(range(self.labyrinth.num_rows), repeat=2)]
        wormholes = random.sample(holes, 5)
        # treasure.append(self.labyrinth.generation_path[random.randint(1, self.labyrinth.num_rows)])
        print(f'wormholes location: {wormholes}')
        return wormholes
