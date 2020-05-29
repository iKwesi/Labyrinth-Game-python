from abc import ABC, abstractmethod

class IGameObject(ABC):
    @abstractmethod
    def __str__(self) -> str: pass

    @abstractmethod
    def location(self): pass