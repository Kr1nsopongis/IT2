import pygame 
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a,K_s,K_d)
import os

pygame.init()

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

stjerne = pygame.image.load(absRef("stjernee.png")) 
stjerne = pygame.transform.scale(stjerne, (60,60))



font = pygame.font.SysFont("Arial",20, bold = True)

screen = pygame.display.set_mode((800, 800))


def SkrivTekst(tekst,font,tekstFarge,x,y):
   tekstBoks = font.render(tekst,True, tekstFarge)
   screen.blit(tekstBoks,(x,y))

def printBilde(bilde,x,y):
   screen.blit(bilde,(x,y))

def kollisjonsSkjekk(self):
    if pygame.sprite.spritecollide(self,baller,True):
      print("Hello")

# def finnAvstand(ball, ball2):
#   xAvstand2 = (ball.x - ball2.x)**2  # x-avstand i andre
#   yAvstand2 = (ball.y - ball2.y)**2  # y-avstand i andre
#   avstand = m.sqrt(xAvstand2 + yAvstand2)
#   print(avstand)

  # if avstand == 0:
  #  print("game over")
  #  pygame.quit

class Ball(pygame.sprite.Sprite):
 
  def __init__(self, x, y,lengde,bredde, xFart, yFart):
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    self.lengde = lengde
    self.bredde = bredde
    # self.surf = pygame.Surface((self.lengde,self.bredde))
    self.xFart = xFart
    self.yFart = yFart
    # self.rect = self.surf.get_rect(center = (self.x,self.y))
    

  
  def tegn(self):
    """Metode for å tegne ballen"""
    pygame.draw.rect(screen, (255, 69, 0), pygame.Rect(self.x,self.y,self.lengde,self.lengde)) 

  def rektangel(self):
    SpillerRect = pygame.Rect(self.x,self.y,10,10)
    return SpillerRect

  # def flytt(self, taster):
  #   if taster[K_UP] and self.y > 0:
  #     self.y -= self.yFart
  #   if taster[K_DOWN] and self.y < 800:
  #     self.y += self.yFart
  #   if taster[K_LEFT] and self.x > 0:
  #     self.x -= self.xFart
  #   if taster[K_RIGHT] and self.x < 800:
  #     self.x += self.xFart

  def flytt(self, taster):
    if self.y > 200:
      if taster[K_UP] and self.y > 0:
        self.y -= self.yFart
      if taster[K_DOWN] and self.y < 800:
        self.y += self.yFart
      if taster[K_LEFT] and self.x > 200:
        self.x -= self.xFart
      if taster[K_RIGHT] and self.x < 600:
        self.x += self.xFart
    elif self.y == 200 and self.x<200 or self.x>600:
      # if taster[K_UP] and self.y > 0+self.radius/2:
      #   self.y -= self.yFart
      if taster[K_DOWN] and self.y < 800:
        self.y += self.yFart
      if taster[K_LEFT] and self.x > 0:
        self.x -= self.xFart
      if taster[K_RIGHT] and self.x < 800:
        self.x += self.xFart
    else:
      if taster[K_UP] and self.y > 0:
        self.y -= self.yFart
      if taster[K_DOWN] and self.y < 800:
        self.y += self.yFart
      if taster[K_LEFT] and self.x > 0:
        self.x -= self.xFart
      if taster[K_RIGHT] and self.x < 800:
        self.x += self.xFart

class Ball2(Ball,pygame.sprite.Sprite):
  def __init__(self, x, y,lengde,bredde, xFart, yFart):
    super().__init__(x, y, xFart, yFart,lengde,bredde)
    pygame.sprite.Sprite.__init__(self)
    self.x = x
    self.y = y
    self.lengde = lengde
    self.bredde = bredde
    self.xFart = xFart
    self.yFart = yFart
    self.rect = pygame.Rect(self.x,self.y,10,10)


  def flytt(self):
    if self.x  <= 0 or self.x >= screen.get_width():
      self.xFart = -self.xFart
      # print(self.xFart) 

    if self.y <= 0 or self.y>= screen.get_height():
      self.yFart = -self.yFart
    
  def fart(self): 
    self.x += self.xFart
    self.y += self.yFart

  def ballRektangel(self):
    ballRect = pygame.Rect(self.x,self.y,10,10)
    return ballRect

      
baller = pygame.sprite.Group()
spiller = pygame.sprite.Group()    

# Lager et Ball-objekball = 
ball = Ball(100, 250, 40, 40, 4, 4)
ball2 = Ball2(100, 250, 40, 40, 2, 0)
ball3 = Ball2(100, 300,40, 40, 4, 0)
ball4 = Ball2(100, 350,40, 40, 10, 0)

baller.add(ball2)
baller.add(ball3)
baller.add(ball4)

spiller.add(ball)

fortsett = True
while fortsett:
     # Sjekker om brukeren har lukket vinduet
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        fortsett = False

    stjerneBakgrunn = pygame.draw.rect(screen,(10,10,10),pygame.Rect(370,30,60,60))
    # print(ball.rect,"sdfnfsd.jgnhsdfrøjlhgadefkhjbg")
    # print(ball2.rect)
    
    # for event in pygame.event.get():
    #     print(event)
    

    screen.fill(background)
    screen.blit(bakgrunn, (0,0))
  
    trykkede_taster = pygame.key.get_pressed()

    ball.flytt(trykkede_taster)
    # print(ball.x)
    ball.tegn()
    

    # kollisjonsSkjekk(ball)

    ball2.ballRektangel()
    ball2.flytt()
    ball2.fart()
    ball2.tegn()

    ball3.ballRektangel()
    ball3.flytt()
    ball3.fart()
    ball3.tegn()

    ball4.ballRektangel()
    ball4.flytt()
    ball4.fart()
    ball4.tegn()

    # if SpillerRect(ball).colliderect(ball2.rect):
    #   print("hei")

    printBilde(stjerne,370,30)
    
    pygame.draw.rect(screen, (133,133,133), pygame.Rect(0, 0, 200, 600))
    pygame.draw.rect(screen, (133,133,133), pygame.Rect(600,0, 200, 600))
    SkrivTekst("Gå til stjernen!",font,(0,0,0), 20,100)
    printBilde(stjerne,66,200)


    pygame.display.update()
    clock.tick(60)
    

        
    



