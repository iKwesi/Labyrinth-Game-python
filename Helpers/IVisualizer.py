from abc import ABCMeta, abstractmethod

class IVisualizer(metaclass = ABCMeta):
    """ Interface for showing labyrinth """

    @abstractmethod
    def set_media_filename(self, filename): pass

    @abstractmethod
    def show_labyrinth(self): pass

    @abstractmethod
    def plot_walls(self): pass

    @abstractmethod
    def configure_plot(self): pass