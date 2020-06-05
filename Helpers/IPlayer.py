from abc import ABC, abstractmethod

class IPlayer(ABC):
    
    @abstractmethod
    def get_player_pos(self): pass

    @abstractmethod
    def move(self): pass