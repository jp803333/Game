import pygame
import tokens

class player:
    def __init__(self, color, surface ):
        self.color = color
        self.surface = surface
    def draw(self, x, y):
        self.xcor = x
        self.ycor = y
        dice = tokens.token(self.xcor, self.ycor, self.surface, self.color)
        dice.draw()

