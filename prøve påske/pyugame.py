import pygame as pg 
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import os

pg.init()

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Stjelt av linus

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

background = GRAY
clock = pg.time.Clock()
screen = pg.display.set_mode((800, 800))

class Sirkel:
   
    def __init__(self, x, y, xFart, yFart, radius, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.xFart = xFart
        self.yFart = yFart
        self.radius = radius
        self.vindusobjekt = vindusobjekt
    
    def tegn(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 
    
    def fart(self):
        if self.x == 0 or self.x == 800:
           self.xFart = -self.xFart

        if self.y == 0 or self.y == 800:
           self.yFart = -self.yFart

        self.x += self.xFart
        self.y += self.yFart
        

        

ball = Sirkel(400, 400, 0, 7 , 20, screen)

while True:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        fortsett = False
    
    screen.fill(background)
    ball.fart()
    ball.tegn()
    pg.display.update()
    
    clock.tick(60)