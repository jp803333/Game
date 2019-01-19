import pygame
import sys
import shapes

pygame.init()

size = width, height = 600, 600
bgimage = pygame.image.load('resources\main.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('craap')
screen.fill((0, 0, 255))
screen.blit(bgimage, (0, 0))
newbtn = shapes.buttons(250, 400, 100, 50, screen, (0, 0, 255), 'New Game')

while True:
    newbtn.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()