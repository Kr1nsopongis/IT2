import pygame
import random 

class Player(): 
    def __init__(self,position,hp,weaponDmg):
        self.position = position
        self.hp = hp 
        self.weapon = weaponDmg
    
    # def movement():
    #     retningvalg = []

    #     for i in range(0,len(rom)-1):
    #         if rom[i].mapPositon == Player.position:
    #             retningvalg = rom[i].retninger



class Maps():
    def __init__(self,mapPosition,effekt,timer,retninger):
        self.mapPositionX = mapPosition
        self.effekt = effekt
        self.timer = timer
        self.retninger = retninger 








# Players
player = Player([0,0],100,0)
Boss = Player([random.randint(0,10),random.randint(0,10)],200,0)


# Rooms
rom = ["startRoom","room01","room11"]

#[opp,ned,høyre,venstre]
startRoom = Maps([0,0],"weaponSelect",0,[0,1,2,3])
room01 = Maps([0,1],"none",0,["x","x",3,4])
room11 = Maps([1,1],"trap",5,["x","x","x",4])

retningvalg = []

def movement():
        retningvalg = []

        for i in range(0,len(rom)-1):
            if rom[i].mapPosition == Player.position:
                retningvalg = rom[i].retninger
        print(rentningvalg)

movement()