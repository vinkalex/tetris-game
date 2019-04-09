from Piece1 import Piece
import pygame


class Line(Piece):
    def __init__(self):
        Piece.__init__(self, 4, 1, "line", [[1] * 4 for i in range(1)], 380, (139, 0, 139))

    def print(self, x_coord, y_coord, side, window):
        pygame.draw.rect(window, self.colors, (x_coord, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 40, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 60, y_coord, side, side))

    def type(self):
        return self.types

    def boardd(self):
        return self.board
