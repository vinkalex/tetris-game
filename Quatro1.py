from Piece1 import Piece
import pygame


class Quatro(Piece):
    """Inherited class Quatro"""
    def __init__(self):
        """Method of initialization of inherited class uses method of initialization of parent class
        Field rows is assigned with 2, field columns is assigned with 2, field types if assigned with "square",
        field data is assigned with corresponding matrix,  field board is assigned with 360,
        field color is assigned with (255, 215, 0)"""
        Piece.__init__(self, 2, 2, "square", [[1] * 2 for i in range(2)], 360, (255, 215, 0))

    def print(self, x_coord, y_coord, side, window):
        """Method of printing the figure
        Figure should look like this:
            XX
            XX    """
        pygame.draw.rect(window, self.colors, (x_coord, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord, side, side))
