import pygame

class Player(): 
    def __init__(self,positionX,positionY,hp):
        self.positionX = positionX
        self.positionY = positionY
        self.hp = hp 

class Maps():
    def __init__(self,mapPositionX,mapPositionY,effekt,timer):
        self.mapPositionX = mapPositionX
        self.mapPositionY = mapPositionY
        self.effekt = effekt
        self.timer = timer

player = Player(0,0,100)

room1 = Maps(1,1,"none",0)
room2 = Maps(2,1,"trap",5)

print(player.positionX,player.positionY)