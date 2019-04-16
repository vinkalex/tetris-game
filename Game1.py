from Alone1 import Alone
from Line1 import Line
from Tetra1 import Tetra
from Quatro1 import Quatro
import pygame
import random


class Game():
    """Класс - реализация игровой механики"""
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
        """Метод - инициализация класса игра"""
        pass

    def check_the_lines(self, width, length):
        """Метод
        Входные данные - принимает размеры матрицы игрового поля width и length(элемент равен 1 если клетка занята,
        0 если нет)(числа)
        Проверяет, есть ли в матрице строки, заполненные 1
        Возвращает номер строки (check - число) заполненной 1(если таких строк
        несколько, возвращает номер той, которая выше), если такой строки нет - возвращает -1"""
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
        """Метод
        Входные данные - нет
        Выбирает рандомную фигуру их списка классов заданных фигур"""
        list_of_classes = [Alone, Quatro, Tetra, Line]
        self.figure = random.choice(list_of_classes)()

    def set_the_place_of_figure(self):
        """Метод
        Входные данные - нет
        Рандомно задает координату по х в зависимости от типа заданной фигуры"""
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
        """Метод
        Входные данные - нет
        В зависимости от типа фигуры изменяет переменную condition(число) - проверяет, пуста ли строка под фигурой
        В результате в переменной condition будет 0 - есл строка свободна, либо число - отичное от 0 -
        значит строка под фигурой не свободна для ее перемещения вниз"""
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
        """Метод
        Входные данные - окно, в котором будем работать
        Заливает окно фоновым цветом"""
        win.fill((0, 0, 0))

    def print_the_screen_and_figure(self, win):
        """Метод
        Входные данные - окно, в котором будем работать
        Метод отрисовывает в окне весь графический интерфейс - клеточки, окно со счетом игры, игровое поле,
        фигуру в данный момент времени"""
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
        """Метод
        Входные данные - нет
        Обработка действий с клавиатурой"""
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
        Входные данные - нет
        Изменяет координату фигуры по y - сдвигает всю фигуру на клетку вниз"""
        self.position_y += 20

    def stop_the_figure(self):
        """Метод
        Входные данные - нет
        Метод - обработка остановки фигуры, изменяет матрицу игрового поля в соответствии с данным конечным
        положением фигуры(заполняет элементы текущего положения единицами"""
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
        Входные данные - нет
        Метод удаляет все строки матрицы игрового поля, заполненные единицами, если таковые есть
        в соответствии с этим меняет счет игры"""
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
        """Метод
        Входные данные - окно, в котором будем работать
        Метод отрисовывает заполненное на данный момент игровое поле"""
        for i in range(11):
            for j in range(16):
                if self.lst[i][j] == 1:
                    pygame.draw.rect(win, (0, 0, 255), (150 + (i * 20) + 1, (100 + (j * 20)) + 1, 20 - 1, 20 - 1))
        self.position_y = 80

    def run(self):
        """Метод, запускающий игру
        Входные данные - нет
        использует все вышеперечисленные методы, описывает игровую механику"""
        pygame.init()
        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Cubes Game")

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
