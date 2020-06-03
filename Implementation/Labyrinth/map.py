import random

from Helpers.IGameObject import IGameObject

# from Implementation.Labyrinth.labyrinth import Labyrinth

class Map(IGameObject):
    def __init__(self, labyrinth):
        self.name = 'Map'
        self.labyrinth = labyrinth
    
    def __str__(self):
        return self.name

    def location(self):
        map = []
        map.append(self.labyrinth.generation_path[random.randint(1, self.labyrinth.num_rows)])
        print(f'Map location: {map}')
        return map
