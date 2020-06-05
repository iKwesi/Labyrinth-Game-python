import random

from Helpers.IGameObject import IGameObject

# from Implementation.Labyrinth.labyrinth import Labyrinth

class Treasure(IGameObject):
    def __init__(self, labyrinth):
        self.name = 'Treasure'
        self.labyrinth = labyrinth
    
    def __str__(self):
        return self.name

    def location(self):
        treasure = []
        treasure.append(self.labyrinth.generation_path[random.randint(1, self.labyrinth.num_rows)])
        # print(f'Treasure location: {treasure}')
        return treasure
