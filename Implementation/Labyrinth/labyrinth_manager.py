import random

from Implementation.Labyrinth.labyrinth import Labyrinth
from Implementation.Labyrinth.labyrinth_visualizer import Visualizer
from Implementation.Labyrinth.Player import Player
from Implementation.Labyrinth.Bear import Bear
from Implementation.Labyrinth.treasure import Treasure


from Helpers.ILabyrinth_Manager import ILabyrinth_Manager
from Helpers.Direction import Direction

class LabyrinthManager(ILabyrinth_Manager):
    """ Class that abstracts interaction with the component """

    def __init__(self):
        self.labyrinths = []
        self.media_name = ""
        # self.player_moved = False

    def add_labyrinth(self, row, col, id = 0):
        """ Add a labyrinth to the manager """

        if id != 0:
            self.labyrinths.append(Labyrinth(row, col, id)) 
        else:
            if len(self.labyrinths) < 1:
                self.labyrinths.append(Labyrinth(row, col, 0))
            else:
                self.labyrinths.append(Labyrinth(row, col, len(self.labyrinths) + 1))

        return self.labyrinths[-1]

    def add_existing_labyrinth(self, labyrinth, override = True):
        """ Add already existing labyrinth to manager """

        # Check if there is a labyrinth with the same id. If there is a conflict, return False
        if self.check_matching_id(labyrinth.id) is None:
            if override:
                if len(self.labyrinths) < 1:
                    labyrinth.id = 0
                else:
                    labyrinth.id = self.labyrinths.__len__()+1
        else:
            return False
        self.labyrinths.append(labyrinth)
        return labyrinth

    def check_matching_id(self, id):
        """Check if the id already belongs to an existing labyrinth

        Args:
            id (int): The id to be checked

        Returns:

        """
        return next((labyrinth for labyrinth in self.labyrinths if labyrinth .id == id), None)

    def get_labyrinth(self, id): 
        """ Get a labyrinth by its id """

        for labyrinth in self.labyrinths:
            if labyrinth.id == id:
                return labyrinth
        print("Unable to locate labyrinth")
        return None

    def get_all_labyrinth(self):
        """Get all of the labyrinths that the manager is holding"""
        
        return self.labyrinths

    def get_labyrinth_count(self):
        """Gets the number of labyrinths that the manager is holding"""
        return self.labyrinths.__len__()

    def show_labyrinth(self, id, cell_size = 1): 
        """Just show the generation animation and labyrinth"""
        # pylint: disable = no-value-for-parameter
        vis = Visualizer(self.get_labyrinth(id), cell_size, self.media_name)
        vis.show_labyrinth()

    def show_labyrinth_play(self, id, cell_size = 1):
        """ Show the player move on labyrinth"""
        vis = Visualizer(self.get_labyrinth(id), cell_size, self.media_name)
        vis.show_labyrinth_play()
        
    def set_filename(self, filename):
        """
        Sets the filename for saving animations and images
        Args:
            filename (string): The name of the file without an extension
        """

        self.media_name = filename


    def play_movement(self,lab_id, move):

        lab = self.get_labyrinth(lab_id)
        return lab.place_player(move)

    
    def bear_movement(self,lab_id, move):

        lab = self.get_labyrinth(lab_id)
        
        return lab.place_bear(move)

    # def next_wormhole(self, lab_id):
    #     lab = self.get_labyrinth(lab_id):
    #     return lab.

    def next_wormhole(self,lab_id):
        lab = self.get_labyrinth(lab_id)
        return lab.next_wormhole()

        # return lab.next_hole

        # player = Player(lab)
        # # if move == Direction.Up.name:
        # player.move('Up') # get user input
        # player.move('Left')
            
