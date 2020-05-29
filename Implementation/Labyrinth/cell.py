from Helpers.ICell import ICell

class Cell(ICell):
    """ A class for repping a cell as a grid """

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.active = False
        self.is_entry_exit = None
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.neighbours = []

    def is_walls_between(self, neighbour):
        """ A function to check if there are walls between self and a neighbour cell.
        Returns True if there are walls else False
        """

        if self.row - neighbour.row == 1 and self.walls['top'] and neighbour.walls['bottom']:
            return True

        elif self.row - neighbour.row == -1 and self.walls['bottom'] and neighbour.walls['top']:
            return True
        
        elif self.col - neighbour.col == 1 and self.walls['left'] and neighbour.walls['right']:
            return True
        elif self.col - neighbour.col == -1 and self.walls['right'] and neighbour.walls['left']:
            return True
        
        return False

    def remove_walls(self, neighbour_row, neighbour_col):
        """ Function to remove walls between neighbour cell and the current cell """

        if self.row - neighbour_row == 1:
            self.walls["top"] = False
            return True, ""
        elif self.row - neighbour_row == -1:
            self.walls["bottom"] = False
            return True, ""
        elif self.col - neighbour_col == 1:
            self.walls["left"] = False
            return True, ""
        elif self.col - neighbour_col == -1:
            self.walls["right"] = False
            return True, ""
        return False

    def set_as_entry_exit(self, entry_exit, row_limit, col_limit):
        """Function that sets the cell as an entry/exit cell by
        removing the outer boundary wall.
        """

        if self.row == 0:
            self.walls["top"] = False
        elif self.row == row_limit:
            self.walls["bottom"] = False
        elif self.col == 0:
            self.walls["left"] = False
        elif self.col == col_limit:
            self.walls["right"] = False

        self.is_entry_exit = entry_exit