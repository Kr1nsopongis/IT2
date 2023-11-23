import pygame
import random 

class Player(): 
    def __init__(self,positionX,positionY,hp,weaponDmg):
        self.positionX = positionX
        self.positionY = positionY
        self.hp = hp 
        self.weapon = weaponDmg

class Maps():
    def __init__(self,mapPositionX,mapPositionY,effekt,timer):
        self.mapPositionX = mapPositionX
        self.mapPositionY = mapPositionY
        self.effekt = effekt
        self.timer = timer



def movement():
    

    for i in range(0,random.randint(0,3)):
        retningValg.append(retninger[random.randint(0,len(retninger)-1)])
    
    print(retningValg)

movement()






    



# Players
player = Player(0,0,100,0)
Boss = Player(random.randint(0,10),random.randint(0,10),200,0)

# Rooms
startRoom = Maps(0,0,"weaponSelect",0)
room1 = Maps(1,1,"none",0)
room2 = Maps(2,1,"trap",5)

print(player.positionX,player.positionY)

