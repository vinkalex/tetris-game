from Piece1 import Piece
import pygame


class Line(Piece):
    """Inherited class Line"""
    def __init__(self):
        """Method of initialization of inherited class uses method of initialization of parent class
        Field rows is assigned with 4, field columns is assigned with 1, field types if assigned with "line",
        field data is assigned with corresponding matrix,  field board is assigned with 380,
        field color is assigned with (139, 0, 139)"""
        Piece.__init__(self, 4, 1, "line", [[1] * 4 for i in range(1)], 380, (139, 0, 139))

    def print(self, x_coord, y_coord, side, window):
        """Method of printing the figure
        Figure should look like this:
           XXXX    """
        pygame.draw.rect(window, self.colors, (x_coord, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 40, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 60, y_coord, side, side))
