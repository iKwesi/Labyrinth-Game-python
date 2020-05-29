from __future__ import absolute_import
import sys
import random

sys.path.append('../')

from Helpers.IGame import IGame
from Helpers.Direction import Direction

from Implementation.Labyrinth.labyrinth_manager import LabyrinthManager
from Implementation.Labyrinth.labyrinth import Labyrinth

import pyfiglet

class Game(IGame):
    def __init__(self):
        game_header = pyfiglet.figlet_format("**Labyrinth**") #,font="alligator")
        print(game_header)
        

    def game_initialize(self):
        """ Starts the game by showing list of commands and asking user for labyrinth size 
            start -> to start the game, load <filename>-> to load existing game or quit -> to close game
            show -> to show the labyrinth
        """

        print(f'Here is the list of commands for the game')
        print(f'"start" -> to start a new game')
        # print(f'load <file name>')
        print(f'"quit" -> to close the game')
        print(f'"up", "down", "left", "right" for movement')
        

    def game_start(self):
        playing = True
        while True:

            user_input = input("Do you want to start or load a new game? Type [load] or start or quit: ")
            if user_input.lower() == 'start':
                lab_size = ""
                while (not lab_size.isnumeric()) or int(lab_size) < 4 or int(lab_size) > 10:
                    lab_size = input(f'Please enter labyrinth size from 4 to 10: ')
                lab_size = int(lab_size)

                manager = LabyrinthManager()
                labyrinth = manager.add_labyrinth(lab_size, lab_size)
                manager.show_labyrinth(labyrinth.id) # to be removed

                print(f'You can start playing')
                while playing:
                    user_input = input('Enter_command: ')
                    if user_input.lower() == 'show':
                        manager.show_labyrinth_play(labyrinth.id)
                    elif user_input.lower() in Direction.__members__:
                        manager.play_movement(labyrinth.id, user_input)
                        bear_direction = random.choice(list(Direction))
                        manager.bear_movement(labyrinth.id, bear_direction)
                    elif user_input.lower() == 'quit':
                        user_input = input('Are you sure you want to quit [y/n]: ')
                        if user_input.lower() == 'y':  
                            print('Thank you for playing')
                            break
                    else:
                        print('invalid command') # work on this to get the error message if user enters garbage
                        continue
            
            elif user_input.lower() == 'quit':
                user_input = input('Are you sure you want to quit [y/n]: ')
                if user_input.lower() == 'y':  
                    print('Thank you for playing')
                    break
                else:
                    continue  # work on this
                # sys.exit(0)
        # print(f'Game has started')