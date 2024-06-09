import pygame as p
import math as m
import time

p.init()

clock = p.time.Clock()

window = p.display.set_mode([500,500])

class Player:
    def __init__(self,x,y,speed,windowObject):
        self.x = x
        self.y = y
        self.speed = speed
        self.windowObject = windowObject

    def draw(self):
        p.draw.rect(self.windowObject,(255,0,0),p.Rect(self.x,self.y,60,60))

    def move(self, key):
        print("gå")
        if key[p.K_w]:
            self.y -= self.speed
        if key[p.K_s]:
            self.y += self.speed
        if key[p.K_a]:
            self.x -= self.speed
        if key[p.K_d]:
            self.x += self.speed
        


player = Player(150,150,1,window)

while True:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    window.fill((0, 0, 0))

    player.move(p.key.get_pressed())
    player.draw()
    p.display.flip()
    clock.tick


