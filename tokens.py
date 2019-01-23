import pygame
class token:
    def __init__(self, x, y, surface, color):
        self.xcor = x
        self.ycor = y
        self.screen = surface
        self.color = color
    def draw(self):
        if self.color == 'red':
            image = pygame.image.load('resources\Red.png')
        elif self.color == 'green':
            image = pygame.image.load('resources\Green.png')
        elif self.color == 'yellow':
            image = pygame.image.load('resources\Yellow.png')
        elif self.color == 'blue':
            image = pygame.image.load('resources\Blue.png')
        self.screen.blit(image, (self.xcor-5, self.ycor-5))





