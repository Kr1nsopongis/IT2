import pygame

class Player(): 
    def __init__(self,positionX,positionY):
        self.positionX = positionX
        self.positionY = positionY

class Maps():
    def __init__(self,mapPositionX,mapPositionY):
        self.mapPositionX = mapPositionX
        self.mapPositionY = mapPositionY

room1 = Maps(1,1)
room2 = Maps(2,1)
