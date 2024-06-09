import pygame
import random

# Konstantar for skjermstørrelse
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Game:
    def __init__(self):
        self.objects = []
        # ----
        self.lives = 10

    def spawn_object(self):
        # Legg til eit nytt fallande objekt på ein tilfeldig x-posisjon
        x = random.randint(0, SCREEN_WIDTH)
        speed = random.randint(1, 5)
        self.objects.append(FallingObject(x, speed))

    def update(self):
        # Oppdater alle fallende objekter
        for obj in self.objects:
            obj.update()

            # --
    
    def check_collisions(self, crosshair):
        for obj in self.objects:
            if crosshair.get_rect().colliderect(obj.get_rect()):
                self.objects.remove(self.objects[self.objects.index(obj)])
                pygame.mixer.music.play()
                # while pygame.mixer.music.get_busy() ==True:
                #     pass
                print("Kollisjon!")
                

class Crosshair:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

    def draw(self, screen):
        # Teikn siktekrysset
        pygame.draw.line(screen, (255, 255, 255), (self.x - 10, self.y), (self.x + 10, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y - 10), (self.x, self.y + 10), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x - 10, self.y - 10, 20, 20)

class FallingObject:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed

    def update(self):
        # Flytt objektet nedover
        self.y += self.speed

    def draw(self, screen):
        # Tegn objektet som ein firkant
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x - 10, self.y - 10, 20, 20))

    def get_rect(self):
        return pygame.Rect(self.x - 10, self.y - 10, 20, 20)

class Musikk():
    def __init__(self,navn,filsti):
        self.navn = navn
        self.filsti = filsti






'''
Game loop og hovudprogram
'''
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Lag ein font
font = pygame.font.Font(None, 36)

game = Game()
crosshair = Crosshair()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for objekt in game.objects:
        if game.objects[game.objects.index(objekt)].y == 600 :
            game.objects.remove(game.objects[game.objects.index(objekt)])
            game.lives -= 1
            print("fjernet")
       
    sang1 = Musikk("sang1","Heldagsprøve innlevering/lyd/thump.wav")

    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.7) 
    pygame.mixer.music.load(sang1.filsti)
    

    # Oppdater siktekryssets posisjon til museposisjonen
    crosshair.x, crosshair.y = pygame.mouse.get_pos()

    # Spawne nye objekt med ein viss sannsynlegheit kvar frame
    if random.random() < 0.03: # tredobled sjansen for atfalling object spawner. 
        game.spawn_object()

    game.update()

    game.check_collisions(crosshair)

    screen.fill((0, 0, 0))
    for obj in game.objects:
        obj.draw(screen)
    crosshair.draw(screen)

    # Teikn antall liv på skjermen
    lives_text = font.render(f"Lives: {game.lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))


    pygame.display.flip()

    clock.tick(60)

    if game.lives < 1:
        running = False

pygame.quit()