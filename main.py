import pygame
import sys
from shapes import buttons as btn
import startgame


pygame.init()

size = width, height = 600, 600
sts = 0
bgimage = pygame.image.load('resources\main.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('craap')
screen.blit(bgimage, (0, 0))

while True:
    if sts == 0:
        mouse = pygame.mouse.get_pos()
        if 350 >= mouse[0] > 250 and 450 >= mouse[1] > 400:
            newbtn = btn(250, 400, 100, 50, screen, (0, 0, 255), 'New Game',16)
            newbtn.draw()
            if pygame.mouse.get_pressed()[0]:
                sts = 1
                screen.fill((255, 255, 255))
                newgame = startgame.board(screen)
                newgame.createboard()
        else:
            newbtn = btn(250, 400, 100, 50, screen, (0, 0, 200), 'New Game',16)
            newbtn.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()