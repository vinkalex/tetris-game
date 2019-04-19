from Piece1 import Piece
import pygame


class Alone(Piece):
    """Inherited class Alone"""
    def __init__(self):
        """Method of initialization of inherited class uses method of initialization of parent class
        Field rows is assigned with 1, field columns is assigned with 1, field types if assigned with "alone",
        field data is assigned with corresponding matrix,  field board is assigned with 380,
        field color is assigned with (0, 255, 127)"""
        Piece.__init__(self, 1, 1, "alone", [[1] * 1 for i in range(1)], 380, (0, 255, 127))

    def print(self, x_coord, y_coord, side, window):
        """Method of printing the figure
        Figure should look like this:
          X """
        pygame.draw.rect(window, self.colors, (x_coord, y_coord, side, side))
