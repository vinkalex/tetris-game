class Piece():
    """Parent class which we will use to inherit classes"""
    def __init__(self, row, column, types, list, Board, Colors):
        """Method of initialization of parent class, takes the amount of lines(numeric), columns of figure(numeric),
        matrix, which is filled with 0 and 1(two-dimensional list),
        maximum value of coordinate yin order not to go beyond the field(numeric) and color of figure(line)"""
        self.rows = row
        self.columns = column
        self.types = types
        self.data = list
        self.board = Board
        self.colors = Colors

    def print(self, x_coord, y_coord, side, window):
        """Figure drawing method : takes x and y coordinates of figure(numeric),
        length of the side of one square(numeric), window in which we will draw"""
        pass

    def type(self):
        """Method which returns the type of the figure(line)"""
        return self.types

    def boardd(self):
        """Method which returns maximum value of y coordinate in order not to go beyond the field (numeric)"""
        return self.board
