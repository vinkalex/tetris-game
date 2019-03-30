import pygame
import random


def check_lines(list, n, m):
    check = -1
    for i in range(0, m - 1):
        flag = 1
        for j in range(0, n - 1):
            if list[j][i] == 0:
                flag = 0
        if flag == 1:
                check = i
    return check


pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Cubes Game")

lst = [[0] * 16 for i in range(11)]
score = 0

x = random.choice([150, 170, 190, 210, 230, 250, 270, 290, 310, 330])
y = 100
side = 20

run = True
while run:
    while lst[(x - 150) // 20][((y+20) - 100) // 20] == 0 and y < 380:
        win.fill((0, 0, 0))

        font = pygame.font.Font(None, 25)
        text = font.render("TOTAL SCORE:", True, (255, 255, 255))
        win.blit(text, [190, 435])
        pygame.draw.line(win, (0, 255, 0), (180, 420), (345, 420), 1)
        pygame.draw.line(win, (0, 255, 0), (180, 465), (345, 465), 1)
        pygame.draw.line(win, (0, 255, 0), (180, 420), (180, 465), 1)
        pygame.draw.line(win, (0, 255, 0), (345, 420), (345, 465), 1)
        font1 = pygame.font.Font(None, 25)
        text1 = font1.render(str(score), True, (0, 255, 0))
        win.blit(text1, [320, 435])

        pygame.draw.rect(win, (0, 0, 255), (x, y, side, side))

        xstart = 150
        ystart = 100

        for i in range(11):
            pygame.draw.line(win, (255, 255, 255), (xstart, 100), (xstart, 400), 1)
            xstart += 20

        for i in range(16):
            pygame.draw.line(win, (255, 255, 255), (150, ystart), (350, ystart), 1)
            ystart += 20

        for i in range(11):
            for j in range(16):
                if lst[i][j] == 1:
                    pygame.draw.rect(win, (0, 0, 255), (150 + (i * 20) + 1, (100 + (j * 20)) + 1, side - 1, side - 1))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 150:
            x -= 20
        if keys[pygame.K_RIGHT] and x < 330:
            x += 20

        y += 20
        pygame.time.delay(300)

        pygame.display.update()

    flag = 1
    for i in range(11):
        if lst[i][0] == 1:
            flag = 0
    if flag == 0:
        break

    lst[(x - 150) // 20][(y - 100) // 20] = 1

    while check_lines(lst, 11, 16) != -1:
        i = check_lines(lst, 11, 16)
        while i >= 1:
            for j in range(11):
                lst[j][i] = lst[j][i - 1]
            i -= 1
        for k in range(11):
            lst[k][0] = 0
        score += 10

    for i in range(11):
        for j in range(16):
            if lst[i][j] == 1:
                pygame.draw.rect(win, (0, 0, 255), (150 + (i * 20) + 1, (100 + (j * 20)) + 1, side - 1, side - 1))

    x = random.choice([150, 170, 190, 210, 230, 250, 270, 290, 310, 330])
    y = 100


pygame.quit()
