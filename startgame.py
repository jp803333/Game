import pygame, sys
class board:
    def __init__(self, surface):
        self.surface = surface
    def createboard(self):
        boardimage = pygame.image.load('resources\Ludo_board.jpg')
        self.surface.blit(boardimage, (50, 50))
