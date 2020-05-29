import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

from PIL import Image

# from multipledispatch import dispatch


from Helpers.IVisualizer import IVisualizer

from Implementation.Labyrinth import labyrinth_manager

class Visualizer(IVisualizer):
    """ A class for showing the labyrinth """

    def __init__(self, labyrinth, cell_size, media_filename):
        self.labyrinth = labyrinth
        self.cell_size = cell_size
        self.height = labyrinth.num_rows * cell_size
        self.width = labyrinth.num_cols * cell_size
        self.ax = None
        self.lines = dict()
        self.squares = dict()
        self.media_filename = media_filename
        self.has_moved = False

    def set_media_filename(self, filename):
        """Sets the filename """
        self.media_filename = filename

    # @dispatch()
    def show_labyrinth(self):
        """Displays a plot of the labyrinth """

        # Create the plot figure and style the axes
        fig = self.configure_plot()

        # Plot the walls on the figure
        self.plot_walls()

        

        # plot the treasure
        self.plot_treasure()

        # plot the player

        self.plot_player()

        self.plot_bear()

        # Display the plot to the user
        plt.show()

        # Handle any potential saving
        if self.media_filename:
            fig.savefig("{}{}.png".format(self.media_filename, "_generation"), frameon=None)

# ------------------------------------------------
    def show_labyrinth_play(self):
        """Displays a plot of the labyrinth """

        # Create the plot figure and style the axes
        fig = self.configure_plot()

        # Plot the walls on the figure
        self.plot_walls()

        # plot the treasure
        self.plot_treasure()

        # plot the player

        self.plot_player_move()

        # plot the bear
        self.plot_bear_move()

        # Display the plot to the user
        plt.show()

        # Handle any potential saving
        if self.media_filename:
            fig.savefig("{}{}.png".format(self.media_filename, "_generation"), frameon=None)   
#  ------------------------------------------------

    def plot_walls(self):
        """ Plots the walls of a labyrinth. This is used when generating the labyrinth image"""
        for i in range(self.labyrinth.num_rows):
            for j in range(self.labyrinth.num_cols):
                if self.labyrinth.initial_grid[i][j].is_entry_exit == "entry":
                    self.ax.text(j*self.cell_size, i*self.cell_size, "START", fontsize=7, weight="bold")
                elif self.labyrinth.initial_grid[i][j].is_entry_exit == "exit":
                    self.ax.text(j*self.cell_size, i*self.cell_size, "END", fontsize=7, weight="bold")
                if self.labyrinth.initial_grid[i][j].walls["top"]:
                    self.ax.plot([j*self.cell_size, (j+1)*self.cell_size],
                                 [i*self.cell_size, i*self.cell_size], color="k")
                if self.labyrinth.initial_grid[i][j].walls["right"]:
                    self.ax.plot([(j+1)*self.cell_size, (j+1)*self.cell_size],
                                 [i*self.cell_size, (i+1)*self.cell_size], color="k")
                if self.labyrinth.initial_grid[i][j].walls["bottom"]:
                    self.ax.plot([(j+1)*self.cell_size, j*self.cell_size],
                                 [(i+1)*self.cell_size, (i+1)*self.cell_size], color="k")
                if self.labyrinth.initial_grid[i][j].walls["left"]:
                    self.ax.plot([j*self.cell_size, j*self.cell_size],
                                 [(i+1)*self.cell_size, i*self.cell_size], color="k")

    def plot_treasure(self):
        img = mpimg.imread('./treasure.jpg')
        imagebox = OffsetImage(img, zoom = 0.3)
        coord = self.labyrinth.treasure
        # ab = AnnotationBbox(imagebox, (0.5 + self.labyrinth.treasure[0][1],
        #                         0.5 + self.labyrinth.treasure[0][0]))
        ab = AnnotationBbox(imagebox, (0.5 + coord[0][1],
                                0.5 + coord[0][0]))
        
        self.ax.add_artist(ab)
        plt.draw()

    def plot_player(self):
        # player_img = mpimg.imread('./player.png')

        path_img2 = '/Users/rapha/Downloads/Documents/Software_Engineering/player.png'

        img2 = Image.open(path_img2).resize((80,90), Image.ANTIALIAS)
        # img2 = img2.resize((80,90),Image.ANTIALIAS)
        coord = self.labyrinth.place_player()
        imagebox = OffsetImage(img2, zoom = 0.4)
        ab2 = AnnotationBbox(imagebox, (0.5 + coord[1],
                                        0.5 + coord[0]))
        # ab2 = AnnotationBbox(imagebox, (0.5 + self.labyrinth.player_pos[0],
        #                                 0.5 + self.labyrinth.player_pos[1]))
        self.ax.add_artist(ab2)
        plt.draw()

    def plot_player_move(self):
        path_img2 = '/Users/rapha/Downloads/Documents/Software_Engineering/player.png'

        img2 = Image.open(path_img2)
        img2 = img2.resize((80,90),Image.ANTIALIAS)
        coord = self.labyrinth.player.player_curr_pos
        imagebox = OffsetImage(img2, zoom = 0.4)
        ab2 = AnnotationBbox(imagebox, (0.5 + coord[1],
                                        0.5 + coord[0]))
        # ab2 = AnnotationBbox(imagebox, (0.5 + self.labyrinth.player_pos[0],
        #                                 0.5 + self.labyrinth.player_pos[1]))
        self.ax.add_artist(ab2)
        plt.draw()        

    def plot_bear(self):
        # player_img = mpimg.imread('./player.png')

        path_img2 = '/Users/rapha/Downloads/Documents/Software_Engineering/bear.png'

        img2 = Image.open(path_img2)
        img2 = img2.resize((80,90),Image.ANTIALIAS)
        coord = self.labyrinth.place_bear()
        imagebox = OffsetImage(img2, zoom = 0.4)
        ab2 = AnnotationBbox(imagebox, (0.5 + coord[1],
                                        0.5 + coord[0]))
        # ab2 = AnnotationBbox(imagebox, (0.5 + self.labyrinth.player_pos[0],
        #                                 0.5 + self.labyrinth.player_pos[1]))
        self.ax.add_artist(ab2)
        plt.draw()

    def plot_bear_move(self):
        path_img2 = '/Users/rapha/Downloads/Documents/Software_Engineering/bear.png'

        img2 = Image.open(path_img2)
        img2 = img2.resize((80,90),Image.ANTIALIAS)
        coord = self.labyrinth.bear.bear_curr_pos
        imagebox = OffsetImage(img2, zoom = 0.4)
        ab2 = AnnotationBbox(imagebox, (0.5 + coord[1],
                                        0.5 + coord[0]))
        # ab2 = AnnotationBbox(imagebox, (0.5 + self.labyrinth.player_pos[0],
        #                                 0.5 + self.labyrinth.player_pos[1]))
        self.ax.add_artist(ab2)
        plt.draw() 

    def configure_plot(self):
        """Sets the initial properties of the labyrinth plot. Also creates the plot and axes"""

        # Create the plot figure
        fig = plt.figure(figsize = (7, 7*self.labyrinth.num_rows/self.labyrinth.num_cols))

        # Create the axes
        self.ax = plt.axes()

        # Set an equal aspect ratio
        self.ax.set_aspect("equal")

        # Remove the axes from the figure
        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.axes.get_yaxis().set_visible(False)
        
        # pylint: disable=unused-variable
        title_box = self.ax.text(0, self.labyrinth.num_rows + self.cell_size + 0.1,
                            r"{}$\times${}".format(self.labyrinth.num_rows, self.labyrinth.num_cols),
                            bbox={"facecolor": "gray", "alpha": 0.5, "pad": 4}, fontname="serif", fontsize=15)

        return fig