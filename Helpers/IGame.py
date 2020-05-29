from abc import ABC, abstractmethod

class IGame(ABC):
    @abstractmethod
    def game_initialize(self): pass

    @abstractmethod
    def game_start(self): pass