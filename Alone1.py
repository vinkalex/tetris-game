from Piece1 import Piece
import pygame


class Alone(Piece):
    def __init__(self):
        Piece.__init__(self, 1, 1, "alone", [[1] * 1 for i in range(1)], 380, (0, 255, 127))

    def print(self, x_coord, y_coord, side, window):
        pygame.draw.rect(window, self.colors, (x_coord, y_coord, side, side))

    def type(self):
        return self.types

    def boardd(self):
        return self.board
