import pygame, sys
from shapes import buttons as btn

class board:
    def __init__(self, surface):
        self.surface = surface
        pass
    def createboard(self):
        boardimage = pygame.image.load('resources\Board.png')
        self.surface.blit(boardimage, (50, 50 ))
        button = btn(275, 12, 50, 25, self.surface, (0, 0, 255),'Quit',14)
        button.draw()