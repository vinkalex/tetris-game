from Piece1 import Piece
import pygame


class Tetra(Piece):
    def __init__(self):
        lst = [[0, 1, 0], [1, 1, 1]]
        Piece.__init__(self, 3, 2, "tetra", lst, 360, (220, 20, 60))

    def print(self, x_coord, y_coord, side, window):
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 40, y_coord + 20, side, side))

    def type(self):
        return self.types

    def boardd(self):
        return self.board
