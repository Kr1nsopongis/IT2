import pygame 
import math as m

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

pygame.init()
screen = pygame.display.set_mode((800, 800))
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

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.xFart = -self.xFart
      print(self.xFart)

    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.yFart = -self.yFart
    
    # Flytter ballen
    self.x += self.xFart
    self.y += self.yFart

# Lager et Ball-objekt
ball = Ball(350, 250, 1, 1 , 20, screen)
ball2 = Ball(100, 250, 1, 1, 20, screen)




while True:
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

    def finnAvstand(ball, ball2):
        xAvstand2 = (ball.x - ball2.x)**2  # x-avstand i andre
        yAvstand2 = (ball.y - ball2.y)**2  # y-avstand i andre
        avstand = m.sqrt(xAvstand2 + yAvstand2)

        # print(avstand)

        if avstand <= ball.radius+ball2.radius:

           ball.xFart = -ball.xFart*1.05
           ball.yFart = -ball.yFart*1.1
           ball2.xFart = -ball2.xFart*1.3
           ball2.yFart = -ball2.yFart*0.9


           

        return avstand

    finnAvstand(ball, ball2)

    # pygame.draw.circle(screen, (255, 0, 0), (100, 250), 50)
    ball.flytt()
    ball2.flytt()
    ball.tegn()
    ball2.tegn()

    pygame.display.update()
    

        
    



