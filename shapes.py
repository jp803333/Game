import pygame, sys
class buttons:
    def __init__(self, x, y, width, height, surface, color, text ,fontsize):
        self.xcor = x
        self.ycor = y
        self.bname = text
        self.width = width
        self.height = height
        self.surface = surface
        self.color = color
        self.fontsize = fontsize

    def draw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.xcor, self.ycor, self.width, self.height))
        if self.bname != None:
            fontobj = pygame.font.Font('freesansbold.ttf', self.fontsize)
            displayfont = fontobj.render(self.bname, True, [255, 255, 255])
            disrect = displayfont.get_rect()
            disrect.center = (self.xcor + self.width/2, self.ycor + self.height/2 )
            self.surface.blit(displayfont, disrect)