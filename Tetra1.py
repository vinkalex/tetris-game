from Piece1 import Piece
import pygame


class Tetra(Piece):
    """Inherited class Tetra"""
    def __init__(self):
        """Method of initialization of inherited class uses method of initialization of parent class
        Field rows is assigned with 3, field columns is assigned with 2, field types if assigned with "tetra",
        field data is assigned with corresponding matrix,  field board is assigned with 360,
        field color is assigned with (220, 20, 60)"""
        lst = [[0, 1, 0], [1, 1, 1]]
        Piece.__init__(self, 3, 2, "tetra", lst, 360, (220, 20, 60))

    def print(self, x_coord, y_coord, side, window):
        """Method of printing the figure
        Figure should look like this:
            X
           XXX    """
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 40, y_coord + 20, side, side))

