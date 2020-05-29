from abc import ABC, abstractmethod

class ILabyrinth_Manager(ABC):
    """ Interface for labyrinth manager"""

    @abstractmethod
    def add_labyrinth(self, row, col, id = 0): pass

    @abstractmethod
    def add_existing_labyrinth(self, labyrinth, override = True):pass

    @abstractmethod
    def get_labyrinth(self, id): pass

    @abstractmethod
    def get_all_labyrinth(self): pass

    @abstractmethod
    def show_labyrinth(self, id, cell_size): pass

    @abstractmethod
    def get_labyrinth_count(self): pass

    @abstractmethod
    def set_filename(self, filename): pass

