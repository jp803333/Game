import pygame
class token:
    def __init__(self, x, y, surface, color):
        self.xcor = x
        self.ycor = y
        self.screen = surface
        self.color = color
    def draw(self):
        if self.color == 1:
            image = pygame.image.load('resources\Redtoken.png')
        elif self.color == 2:
            image = pygame.image.load('resources\Greentoken.png')
        elif self.color == 3:
            image = pygame.image.load('resources\Bluetoken.png')
        elif self.color == 4:
            image = pygame.image.load('resources\yellowtoken.png')
        self.screen.blit(image, (self.xcor, self.ycor))


