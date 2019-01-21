import pygame
import sys
import startgame
import buttons
import random

pygame.init()

size = width, height = 600, 600
bgimage = pygame.image.load('resources\main.png')
screen = pygame.display.set_mode(size)
pygame.display.set_caption('craap')

def newgame():
     global  sts
     sts = 1
def exit():
    pygame.quit()
    sys.exit()
def quitgame():
    global sts
    sts = 0
def Throw():
    global draw
    draw = random.randint(1, 6)

sts = 0
draw = 1

pcolor = [46, 64, 83]
acolor = [52, 73, 94]

newbtn = buttons.Buttons(250, 300, 100, 50, screen, acolor, pcolor, 'New Game', 16, newgame)
exitbtn = buttons.Buttons(250, 400, 100, 50, screen, acolor, pcolor, 'Exit', 16, exit)
quitbtn = buttons.Buttons(400, 10, 100, 30, screen, acolor, pcolor, 'Quit Game', 14, quitgame)
dicebtn = buttons.Buttons(100, 10, 100, 30, screen, acolor, pcolor, 'Throw Dice', 14, Throw)

diceimg = {1: pygame.image.load('resources\dice1.png'),
                 2: pygame.image.load('resources\dice2.png'),
                 3: pygame.image.load('resources\dice3.png'),
                 4: pygame.image.load('resources\dice4.png'),
                 5: pygame.image.load('resources\dice5.png'),
                 6: pygame.image.load('resources\dice6.png')}

while True:
    if sts == 0:
        screen.blit(bgimage, (0, 0))
        newbtn.Draw()
        exitbtn.Draw()

    if sts == 1:
        screen.fill((255, 255, 255))
        newgame = startgame.board(screen)
        newgame.createboard()
        quitbtn.Draw()
        dicebtn.Draw()
        screen.blit(diceimg.get(draw), (275, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()