from Piece1 import Piece
import pygame


class Quatro(Piece):
    def __init__(self):
        Piece.__init__(self, 2, 2, "square", [[1] * 2 for i in range(2)], 360, (255, 215, 0))

    def print(self, x_coord, y_coord, side, window):
        pygame.draw.rect(window, self.colors, (x_coord, y_coord, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord, y_coord + 20, side, side))
        pygame.draw.rect(window, self.colors, (x_coord + 20, y_coord, side, side))

    def type(self):
        return self.types

    def boardd(self):
        return self.board
