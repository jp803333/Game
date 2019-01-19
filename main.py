import pygame
from pygame.draw import  circle as cir
import sys
from shapes import buttons as btn
import startgame
import tokens


pygame.init()

size = width, height = 600, 600
sts = 0
bgimage = pygame.image.load('resources\main.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('craap')

while True:
    if sts == 0:
        screen.blit(bgimage, (0, 0))
        newbtn1 = btn(250, 300, 100, 50, screen, (0, 0, 200), 'New Game', 16)
        newbtn1.draw()
        mouse = pygame.mouse.get_pos()
        if 350 >= mouse[0] > 250 and 350 >= mouse[1] > 300:
            newbtn1 = btn(250, 300, 100, 50, screen, (0, 0, 255), 'New Game', 16)
            newbtn1.draw()
            if pygame.mouse.get_pressed()[0]:
                sts = 1
        else:
            newbtn1 = btn(250, 300, 100, 50, screen, (0, 0, 200), 'New Game', 16)
            newbtn1.draw()

        if 350 >= mouse[0] > 250 and 450 >= mouse[1] > 400:
            newbtn1 = btn(250, 400, 100, 50, screen, (0, 0, 255), 'Exit', 16)
            newbtn1.draw()
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        else:
            newbtn1 = btn(250, 400, 100, 50, screen, (0, 0, 200), 'Exit', 16)
            newbtn1.draw()

    if sts == 1:
        screen.fill((255, 255, 255))
        newgame = startgame.board(screen)
        newgame.createboard()
        newbtn = btn(275, 12, 50, 25, screen, (0, 0, 255), 'Quit', 14)
        newbtn.draw()
        mouse = pygame.mouse.get_pos()
        if 325 >= mouse[0] > 275 and 37 >= mouse[1] > 12:
            newbtn = btn(275, 12, 50, 25, screen, (0, 0, 255), 'Quit', 14)
            newbtn.draw()
            if pygame.mouse.get_pressed()[0]:
                sts = 0
        else:
            newbtn = btn(275, 12, 50, 25, screen, (0, 0, 200), 'Quit', 14)
            newbtn.draw()
        red = (tokens.token(185, 435, screen, 1),tokens.token(151, 402, screen, 1), tokens.token(121, 434, screen, 1), tokens.token(151, 471, screen, 1))
        redcor = ([190,440], [156,407], [126,439],  [156,476], )
        for i in range(4):
            red[i].draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()