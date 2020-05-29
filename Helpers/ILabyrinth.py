from abc import ABC, abstractmethod

class ILabyrinth(ABC):
    """ Interface for creating a maze object """

    @abstractmethod
    def generate_grid(self): pass

    @abstractmethod
    def find_neighbours(self, row, col): pass

    @abstractmethod
    def _validate_neighbours_generate(self, neighbour_indices): pass

    @abstractmethod
    def _pick_random_entry_exit(self, used_entry_exit = None): pass

    @abstractmethod
    def generate_labyrinth(self, start_coor = (0, 0)): pass

    @abstractmethod
    def check_monolith(self, row, col): pass