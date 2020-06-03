import random
import time

from Implementation.Labyrinth.cell import Cell
from Implementation.Labyrinth.treasure import Treasure
from Implementation.Labyrinth.Player import Player
from Implementation.Labyrinth.Bear import Bear
from Implementation.Labyrinth.wormhole import Wormhole
from Implementation.Labyrinth.river import River
from Implementation.Labyrinth.map import Map

from Helpers.ILabyrinth import ILabyrinth

# from multipledispatch import dispatch 

class Labyrinth(ILabyrinth):
    """ Labyrinth class for creating a random labyrinth """

    def __init__(self, num_rows, num_cols, id = 0):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.id = id
        self.grid_size = num_rows * num_cols
        self.entry_coor = self._pick_random_entry_exit(None)
        self.exit_coor = self._pick_random_entry_exit(self.entry_coor)
        self.generation_path = []
        self.solution_path = None
        self.initial_grid = self.generate_grid()
        self.grid = self.initial_grid
        self.generate_labyrinth((0, 0))
        self.treasure = self.place_treasure()
        self.treasure_item = Treasure(self).name
        self.map = self.place_map()
        self.map_item = Map(self).name
        self.player = Player(self)
        self.river = self.place_river()
        self.wormhole = Wormhole(self).location()
        # self.player_pos = ()
        
        self.bear = Bear(self)
        
        # self.player_pos = self.place_player()

    def generate_grid(self): 
        """ function that creates grid of cells """

        grid = []

        # place cell object at each location
        for i in range(self.num_rows):
            grid.append([])

            for j in range(self.num_rows):
                grid[i].append(Cell(i,j))
        
        return grid

    def find_neighbours(self, cell_row, cell_col): 
        """ finds all existing and unvisited neighbours of a cell """
        
        neighbours = []

        def check_neighbour(row, col):
            # check if neighbour exists and is not visited

            if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
                neighbours.append((row, col))

        check_neighbour(cell_row - 1, cell_col) # top neighbour
        check_neighbour(cell_row, cell_col + 1) # right neighbour
        check_neighbour(cell_row + 1, cell_col) # bottom neighbour
        check_neighbour(cell_row, cell_col - 1) # left neighbour

        if len(neighbours) > 0:
            return neighbours
        else:
            return None # no unvisited cells found
        

    def _validate_neighbours_generate(self, neighbour_indices): 
        """ Function that validates if neighbour is visited or not """

        neigh_list = [n for n in neighbour_indices if not self.grid[n[0]][n[1]].visited]

        if len(neigh_list) > 0:
            return neigh_list
        else:
            return None

    def _pick_random_entry_exit(self, used_entry_exit = None): 
        """ Function that picks random coordinates to represent entry or exit """

        rng_entry_exit = used_entry_exit    # Initialize with used value

        # Try until unused location along boundary is found.
        while rng_entry_exit == used_entry_exit:
            rng_side = random.randint(0, 3)

            if (rng_side == 0):     # Top side
                rng_entry_exit = (0, random.randint(0, self.num_cols-1))

            elif (rng_side == 2):   # Right side
                rng_entry_exit = (self.num_rows-1, random.randint(0, self.num_cols-1))

            elif (rng_side == 1):   # Bottom side
                rng_entry_exit = (random.randint(0, self.num_rows-1), self.num_cols-1)

            elif (rng_side == 3):   # Left side
                rng_entry_exit = (random.randint(0, self.num_rows-1), 0)

        return rng_entry_exit       # Return entry/exit that is different from exit/entry
        

    def generate_labyrinth(self, start_coor = (0, 0)): 
        """ Function that takes the grid and remove walls between cells using recursive backtracker algorithm """

        k_curr, l_curr = start_coor             # Where to start generating
        path = [(k_curr, l_curr)]               # To track path of solution
        self.grid[k_curr][l_curr].visited = True     # Set initial cell to visited
        visit_counter = 1                       # To count number of visited cells
        visited_cells = list()   

        print("\nGenerating the labyrinth with depth-first search...")

        while visit_counter < self.grid_size:     # While there are unvisited cells
            neighbour_indices = self.find_neighbours(k_curr, l_curr)    # Find neighbour indicies
            neighbour_indices = self._validate_neighbours_generate(neighbour_indices)

            if neighbour_indices is not None:   # If there are unvisited neighbour cells
                visited_cells.append((k_curr, l_curr))              # Add current cell to stack
                k_next, l_next = random.choice(neighbour_indices)     # Choose random neighbour
                self.grid[k_curr][l_curr].remove_walls(k_next, l_next)   # Remove walls between neighbours
                self.grid[k_next][l_next].remove_walls(k_curr, l_curr)   # Remove walls between neighbours
                self.grid[k_next][l_next].visited = True                 # Move to that neighbour
                k_curr = k_next
                l_curr = l_next 
                path.append((k_curr, l_curr))   # Add coordinates to part of generation path
                visit_counter += 1

            elif len(visited_cells) > 0:  # If there are no unvisited neighbour cells
                k_curr, l_curr = visited_cells.pop()      # Pop previous visited cell (backtracking)
                path.append((k_curr, l_curr))   # Add coordinates to part of generation path

        print("Number of moves performed: {}".format(len(path)))
        
        self.grid[self.entry_coor[0]][self.entry_coor[1]].set_as_entry_exit("entry",
            self.num_rows-1, self.num_cols-1)
        self.grid[self.exit_coor[0]][self.exit_coor[1]].set_as_entry_exit("exit",
            self.num_rows-1, self.num_cols-1)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.grid[i][j].visited = False      # Set all cells to unvisited before returning grid

        self.generation_path = path

    def check_monolith(self,cell_row, cell_col): 
        if (cell_row < 0 or cell_row >= self.num_rows) or (cell_col < 0 or cell_col >= self.num_cols):
            return True
        return False

    #TODO: create service for placing object on labyrinth
    def place_treasure(self):
        # pylint: disable = no-value-for-parameter
        tresh = Treasure(self)
        loc = tresh.location()
        # print(f'treasue: {loc}')
        
        return loc

    def place_map(self):
        map = Map(self)
        loc = map.location()
        # print(f'treasue: {loc}')
        
        return loc
    
    def place_player(self, dir = None):
        # player = Player(self)
        if dir == None:
            player_pos = self.player.get_player_pos()
            # if player_pos == self.place_treasure():
            #     self.player.get_item()
            print(f'player_curr {player_pos}')
            # return self.player_pos
        else:
            player_pos = self.player.get_player_pos(dir)
            # if player_pos == self.place_treasure():
            #     self.player.get_item()
            # player_pos = self.player.player_curr_pos
            # return self.player_pos
        return player_pos


    def place_bear(self, dir = None):
        if dir == None:
            bear_pos = self.bear.get_player_pos()
            print(f'bear_curr {bear_pos}')
           
        else:
            bear_pos = self.bear.get_player_pos(dir)
 
        return bear_pos

    # def place_wormhole(self):
    #     # wormhole = Wormhole(self)
    #     return self.wormhole.location()

    # def next_wormhole(self):
    #     # worm_idx = (self.wormhole.index(self.player.player_curr_pos) + 1) % 5
    #     worm_idx = (self.wormhole.wormholes.index(self.player.player_curr_pos) + 1) % 5
    #     print(f'worm_idx: {worm_idx}')
    #     print(f'next_worm: {self.wormhole.wormholes[worm_idx]}')
    # #     return self.location()[worm_idx]
    #     return self.wormhole.wormholes[worm_idx]

    def next_wormhole(self):
        # worm_idx = (self.wormhole.index(self.player.player_curr_pos) + 1) % 5
        worm_idx = (self.wormhole.index(self.player.player_curr_pos) + 1) % 5
        print(f'worm_idx: {worm_idx}')
        print(f'next_worm: {self.wormhole[worm_idx]}')
        self.player.player_curr_pos  = self.wormhole[worm_idx]
        print(f'player_worm_at: {self.player.player_curr_pos}')
        # return self.wormhole[worm_idx]
        return self.player.player_curr_pos

    def place_river(self):
        riv = River(self)
        river = riv.location()
        return river

    def skip_move(self):
        if self.player.player_curr_pos in self.wormhole:
            self.player.player_curr_pos = self.next_wormhole()
        elif self.player.player_curr_pos in self.river:
            idx = self.river.index(self.player.player_curr_pos)
            if idx + 2 < len(self.river):
                self.player.player_curr_pos = self.river[idx + 2]
                print(f'You moved two steps down the river stream')
            else:
                self.player.player_curr_pos = self.river[-1]
                print(f'You moved to the end of the river')
        else:
            print(f'You skipped your turn')
        return self.player.player_curr_pos