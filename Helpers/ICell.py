from abc import ABC, abstractmethod

class ICell(ABC):
    """ Interface for creating cell object """
   
    @abstractmethod
    def is_walls_between(self, neighbour): pass

    @abstractmethod
    def remove_walls(self, neighbour_row, neighbour_col): pass

    @abstractmethod
    def set_as_entry_exit(self, entry_exit, row_limit, col_limit): pass