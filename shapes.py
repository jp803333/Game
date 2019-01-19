import pygame, sys
class buttons():
    def __init__(self, x, y, width, height, surface, color, text ):
        self.xcor = x
        self.ycor = y
        self.bname = text
        self.width = width
        self.height = height
        self.surface = surface
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.xcor, self.ycor, self.width, self.height))
        if self.bname != None:
            fontobj = pygame.font.Font('freesansbold.ttf', 32)
            displayfont = fontobj.render(self.bname, True, [0, 0, 0], [255, 255, 255])
            disrect = displayfont.get_rect()
            disrect.center = (0, 0)


