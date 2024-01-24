import pygame 
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a,K_s,K_d)
import os

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
clock = pygame.time.Clock()
bakgrunn = pygame.image.load(absRef("Gulv.jpg")) 

screen = pygame.display.set_mode((800, 800))

boks = pygame.draw.circle(screen, (255, 0, 0), (100, 250), 50)


pygame.init()

class Ball:
  """Klasse for å representere en ball"""
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
    pygame.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

  # def flytt(self):
  #   """Metode for å flytte ballen"""
  #   # Sjekker om ballen er utenfor høyre/venstre kant
  #   if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
  #     self.xFart = -self.xFart
  #     print(self.xFart)

  #   if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
  #     self.yFart = -self.yFart

  def flytt(self, taster):
    if taster[K_UP] and self.y > 0+self.radius/2:
      self.y -= self.yFart
    if taster[K_DOWN] and self.y < 800-self.radius/2:
      self.y += self.yFart
    if taster[K_LEFT] and self.x > 0+self.radius/2:
      self.x -= self.xFart
    if taster[K_RIGHT] and self.x < 800-self.radius/2:
      self.x += self.xFart
    
    
      
class Ball2(Ball):
   def __init__(self, x, y, xFart, yFart, radius, vindusobjekt):
      super().__init__(x, y, xFart, yFart, radius, vindusobjekt)
      self.x = x
      self.y = y
      self.xFart = xFart
      self.yFart = yFart
      self.radius = radius
      self.vindusobjekt = vindusobjekt
    
      def fart(self): 
          self.x += self.xFart
          self.y += self.yFart
  #  def flytt(self, taster):
  #   if taster[K_w] and self.y > 0+self.radius/2:
  #     self.y -= self.yFart
  #   if taster[K_s] and self.y < 800-self.radius/2:
  #     self.y += self.yFart
  #   if taster[K_a] and self.x > 0+self.radius/2:
  #     self.x -= self.xFart
  #   if taster[K_d] and self.x < 800-self.radius/2:
  #     self.x += self.xFart 
      
    

# Lager et Ball-objekt
ball = Ball(350, 250, 4, 4 , 20, screen)
ball2 = Ball2(100, 250, 4, 4, 20, screen)



fortsett = True
while fortsett:
     # Sjekker om brukeren har lukket vinduet
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        fortsett = False

    for event in pygame.event.get():
        print(event)
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
                print(background)
            elif event.key == pygame.K_g:
                background = GREEN
                print(background)

    screen.fill(background)
    screen.blit(bakgrunn, (0,0))

    # def finnAvstand(ball, ball2):
    #     xAvstand2 = (ball.x - ball2.x)**2  # x-avstand i andre
    #     yAvstand2 = (ball.y - ball2.y)**2  # y-avstand i andre
    #     avstand = m.sqrt(xAvstand2 + yAvstand2)

    #     # print(avstand)

    #     if avstand <= ball.radius+ball2.radius:

    #        ball.xFart = -ball.xFart*1.01
    #        ball.yFart = -ball.yFart*1.01
    #        ball2.xFart = -ball2.xFart
    #        ball2.yFart = -ball2.yFart


           

    #     return avstand
    
    trykkede_taster = pygame.key.get_pressed()

    # finnAvstand(ball, ball2)

    ball.flytt(trykkede_taster)
    ball2.fart()
    ball.tegn()
    ball2.tegn()

    pygame.display.update()
    clock.tick(60)
    

        
    


