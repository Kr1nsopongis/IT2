import pygame
pygame.init()

class Musikk():
    def __init__(self,navn,filsti):
        self.navn = navn
        self.filsti = filsti

sang1 = Musikk("sang1","lyd/horror.mp3")

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7) 
pygame.mixer.music.load(sang1.filsti)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() ==True:
    pass
