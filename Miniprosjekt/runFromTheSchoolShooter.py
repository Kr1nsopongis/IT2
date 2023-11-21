import pygame

class Player(): 
    def __init__(self,positionX,positionY):
        self.positionX = positionX
        self.positionY = positionY

class Maps():
    def __init__(self,mapPositionX,mapPositionY,effekt,timer):
        self.mapPositionX = mapPositionX
        self.mapPositionY = mapPositionY
        self.effekt = effekt

room1 = Maps(1,1,"none")
room2 = Maps(2,1,"trap",5)
