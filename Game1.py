from Alone1 import Alone
from Line1 import Line
from Tetra1 import Tetra
from Quatro1 import Quatro
import pygame
import random


class Game():
    """Class - implementation of game mechanics"""
    lst = [[0] * 16 for i in range(11)]
    position_x = 0
    position_y = 0
    condition = 0
    side_of_piece = 20
    Run = True
    list_of_classes = [Alone, Quatro, Tetra, Line]
    figure = random.choice(list_of_classes)()
    score = 0

    def __init__(self):
        """Method - initialization of class game"""
        pass

    def check_the_lines(self, width, length):
        """Method
        Input data - takes sizes of matrix of the game field - width and length
        (element's value is 1 if the cell is not empty, 0 else)(numeric)
        Checks, whether the row in the matrix is ​​filled with 1
        Returns line number (check - numeric) which is filled with 1( if it contains several lines of that type,
        returns line number of line which is above), if there is no lines like this - returns -1"""
        check = -1
        for i in range(0, length - 2):
            flag = 1
            for j in range(0, width - 1):
                if self.lst[j][i] == 0:
                    flag = 0
            if flag == 1:
                check = i
        return check

    def choose_the_figure(self):
        """Method
        Input data - none
        Chooses random figure among the list of available figures"""
        list_of_classes = [Alone, Quatro, Tetra, Line]
        self.figure = random.choice(list_of_classes)()

    def set_the_place_of_figure(self):
        """Method
        Input data - none
        Randomly sets x coordinate depending of the type of given figure"""
        self.position_x = 0
        if self.figure.type() == "alone":
            self.position_x = random.choice([150, 170, 190, 210, 230, 250, 270, 290, 310, 330])
        elif self.figure.type() == "square":
            self.position_x = random.choice([150, 170, 190, 210, 230, 250, 270, 290, 310])
        elif self.figure.type() == "tetra":
            self.position_x = random.choice([150, 170, 190, 210, 230, 250, 270, 290])
        elif self.figure.type() == "line":
            self.position_x = random.choice([150, 170, 190, 210, 230, 250, 270])

    def check_the_condition(self):
        """Method
        Input data - none
        Depending on the type of figure changes variable condition(numeric) - checks, whether line under figure is empty
        As a result in variable condition will be 0 - if the line is available or number which is different from 0 -
        it means that line under figure is not available for moving the figure down"""
        self.condition = 0
        if self.figure.type() == "line":
            self.condition = self.lst[(self.position_x - 150) // 20][((self.position_y + 20) - 100) // 20] + \
                             self.lst[(self.position_x - 150 + 20) // 20][((self.position_y + 20) - 100) // 20] + \
                             self.lst[(self.position_x - 150 + 40) // 20][((self.position_y + 20) - 100) // 20] + \
                             self.lst[(self.position_x - 150 + 60) // 20][((self.position_y + 20) - 100) // 20]
        elif self.figure.type() == "alone":
            self.condition = self.lst[(self.position_x - 150) // 20][((self.position_y + 20) - 100) // 20]
        elif self.figure.type() == "square":
            self.condition = self.lst[(self.position_x - 150) // 20][((self.position_y + 40) - 100) // 20] + \
                             self.lst[(self.position_x - 150 + 20) // 20][((self.position_y + 40) - 100) // 20]
        elif self.figure.type() == "tetra":
            self.condition = self.lst[(self.position_x - 150) // 20][((self.position_y + 40) - 100) // 20] + \
                             self.lst[(self.position_x - 150 + 20) // 20][((self.position_y + 40) - 100) // 20] + \
                             self.lst[(self.position_x - 150 + 40) // 20][((self.position_y + 40) - 100) // 20]

    def fill_the_screen(self, win):
        """Method
        Входные данные - window in which we will draw
        Fills the window with background color"""
        win.fill((0, 0, 0))

    def print_the_screen_and_figure(self, win):
        """Method
        Input data - window in which we will draw
        The method draws the entire graphical interface in the window - cells, window with game score, game field,
        figure in current period of time"""
        font = pygame.font.Font(None, 25)
        text = font.render("TOTAL SCORE:", True, (255, 255, 255))
        win.blit(text, [190, 435])
        pygame.draw.line(win, (0, 255, 0), (180, 420), (345, 420), 1)
        pygame.draw.line(win, (0, 255, 0), (180, 465), (345, 465), 1)
        pygame.draw.line(win, (0, 255, 0), (180, 420), (180, 465), 1)
        pygame.draw.line(win, (0, 255, 0), (345, 420), (345, 465), 1)
        font1 = pygame.font.Font(None, 25)
        text1 = font1.render(str(self.score), True, (0, 255, 0))
        win.blit(text1, [320, 435])

        self.figure.print(self.position_x, self.position_y, 20, win)

        xstart = 150
        ystart = 80

        for i in range(11):
            pygame.draw.line(win, (255, 255, 255), (xstart, 80), (xstart, 380), 1)
            xstart += 20

        for i in range(16):
            pygame.draw.line(win, (255, 255, 255), (150, ystart), (350, ystart), 1)
            ystart += 20

        for i in range(11):
            for j in range(16):
                if self.lst[i][j] == 1:
                    pygame.draw.rect(win, (0, 0, 255), (150 + (i * 20) + 1, (100 + (j * 20)) + 1,
                                                        self.side_of_piece - 1, self.side_of_piece - 1))

    def keyboard_event_handling(self):
        """Method
        Input data - none
        Handling keyboard actions"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Run = False

        keys = pygame.key.get_pressed()
        if self.condition == 0 and self.position_y < self.figure.boardd():
            if keys[pygame.K_LEFT] and self.position_x > 150:
                self.position_x -= 20
            if keys[pygame.K_RIGHT]:
                if self.figure.type() == "alone" and self.position_x < 330:
                    self.position_x += 20
                elif self.figure.type() == "square" and self.position_x < 310:
                    self.position_x += 20
                elif self.figure.type() == "tetra" and self.position_x < 290:
                    self.position_x += 20
                elif self.figure.type() == "line" and self.position_x < 270:
                    self.position_x += 20

    def move(self):
        """Метод
        Input data - none
        Changes x and y coordinate - shifts the whole figure down"""
        self.position_y += 20

    def stop_the_figure(self):
        """Метод
        Input data - none
        Method - handling of stop process of the figure, changes game field matrix according to final figure position
        (filling matrix elements with 1)"""
        self.position_y -= 20

        if self.figure.type() == "alone":
            self.lst[(self.position_x - 150) // 20][(self.position_y - 100) // 20] = 1
        elif self.figure.type() == "square":
            self.lst[(self.position_x - 150) // 20][(self.position_y - 100) // 20] = 1
            self.lst[(self.position_x - 150 + 20) // 20][(self.position_y - 100 + 20) // 20] = 1
            self.lst[(self.position_x - 150) // 20][(self.position_y - 100 + 20) // 20] = 1
            self.lst[(self.position_x - 150 + 20) // 20][(self.position_y - 100) // 20] = 1
        elif self.figure.type() == "tetra":
            self.lst[(self.position_x - 150 + 20) // 20][(self.position_y - 100) // 20] = 1
            self.lst[(self.position_x - 150 + 20) // 20][(self.position_y - 100 + 20) // 20] = 1
            self.lst[(self.position_x - 150) // 20][(self.position_y - 100 + 20) // 20] = 1
            self.lst[(self.position_x - 150 + 40) // 20][(self.position_y - 100 + 20) // 20] = 1
        elif self.figure.type() == "line":
            self.lst[(self.position_x - 150 + 20) // 20][(self.position_y - 100) // 20] = 1
            self.lst[(self.position_x - 150 + 60) // 20][(self.position_y - 100) // 20] = 1
            self.lst[(self.position_x - 150) // 20][(self.position_y - 100) // 20] = 1
            self.lst[(self.position_x - 150 + 40) // 20][(self.position_y - 100) // 20] = 1

    def delete_full_lines(self):
        """Метод
        Input data - none
        Deletes all the lines of game field matrix which is filled with 1 if these lines exists,
        and according to this changes game score"""
        if self.check_the_lines(11, 16) != -1:
            i = self.check_the_lines(11, 16)
            while i >= 1:
                for j in range(11):
                    self.lst[j][i] = self.lst[j][i - 1]
                i -= 1
            for k in range(11):
                self.lst[k][0] = 0
                self.lst[k][14] = 0
            self.score += 10

    def print_the_figures(self, win):
        """Method
        Input data - window in which we will draw
        Draws current game field (with the help of game field matrix)"""
        for i in range(11):
            for j in range(16):
                if self.lst[i][j] == 1:
                    pygame.draw.rect(win, (0, 0, 255), (150 + (i * 20) + 1, (100 + (j * 20)) + 1, 20 - 1, 20 - 1))
        self.position_y = 80

    def run(self):
        """Method that runs the game
        Input data - none
        Uses all the methods above, describes the game mechanics"""
        pygame.init()
        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("TETRIS GAME")

        self.choose_the_figure()
        self.set_the_place_of_figure()
        self.position_y = 80

        self.Run = True
        while self.Run:
            self.check_the_condition()
            while self.condition == 0 and self.position_y < self.figure.boardd():
                self.check_the_condition()
                self.fill_the_screen(window)
                self.print_the_screen_and_figure(window)
                self.keyboard_event_handling()
                self.move()
                pygame.time.delay(300)
                pygame.display.update()
            flag = 1
            for i in range(11):
                if self.lst[i][0] == 1:
                    flag = 0
            if flag == 0:
                self.Run = False

            self.stop_the_figure()
            self.delete_full_lines()
            self.print_the_figures(window)
            self.choose_the_figure()
            self.set_the_place_of_figure()
        pygame.quit()
