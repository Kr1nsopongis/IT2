import pygame
import random 
from ascii import *

class Player(): 
    def __init__(self,positionP,hp,weaponDmg):
        self.position = positionP
        self.hp = hp 
        self.weapon = weaponDmg
    

class Maps():
    def __init__(self,mapPosition,effekt,timer,retninger):
        self.mapPosition = mapPosition
        self.effekt = effekt
        self.timer = timer
        self.retninger = retninger 


# Players
player = Player([0,0],100,0)
boss = Player([0,1],200,0)

# random.randint(0,10),random.randint(0,10)

# Rooms
rom = ["startRoom","room01","room11"]

#[opp,ned,høyre,venstre]
startRoom = Maps([0,0],"weaponSelect",0,[0,1,2,3])
room01 = Maps([0,1],"none",0,[3,4])
room11 = Maps([1,1],"trap",5,[4])

def start():
    print(Start)




def movement():
        retningvalg = []
        romRN = ""


        for i in range(0,len(rom)-1):
            if eval(rom[i]).mapPosition == player.position :
                retningvalg = eval(rom[i]).retninger
                romRN = rom[i]
        
        print("\n\nDu står i",romRN,"\n\t0 = Opp \n\t1 = Ned \n\t2 = Høyre\n\t3 = Venstre \n\nDine valg er: ",retningvalg)
        retningInput= input("Skriv inn tallet til ønsket retning:")

        try:
            retningInput = int(retningInput)
        except:
            print("Du må skrive et av disse tallene",retningvalg)
            retningInput= input("Skriv inn tallet til ønsket retning:")

        if retningInput == 0:
            player.position[1] = 1
        elif retningInput == 1:
            player.position[1] -= 1
        elif retningInput == 2:
            player.position[0] += 1
        elif retningInput == 3:
            player.position[0] -= 1
 

        print(player.position)

        return player.position

# def fight():
#     def heal():
#         player.hp += 10
#         return player.hp
    
#     def angrip():
#         boss.hp -= 10
#         return boss.hp
    
#     print("Ånei!!!! Der var det en Boss!!!! \n\nDine valg er: \n\n\t1 = Heal \n\t2 = Angrip")
#     svar = input("Hva velger du?")

#     if svar == 1:
#         heal()
#     elif svar

    

        

# Intro

# start()
movement()
# fight()

