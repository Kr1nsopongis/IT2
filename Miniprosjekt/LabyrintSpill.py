import pygame
import random 
from ascii import *

class Player(): 
    def __init__(self,positionP,hp,weaponDmg):
        self.position = positionP
        self.hp = hp 
        self.weapon = weaponDmg


class Maps():
    def __init__(self,mapPosition,retninger):
        self.mapPosition = mapPosition
        self.retninger = retninger
    
class SpecialMaps(Maps):
    def __init__(self, mapPosition, retninger):
        super().__init__(mapPosition, retninger)
        

# Players
player = Player([0,0],100,0)
boss = Player([0,1],200,0)

# random.randint(0,10),random.randint(0,10)

# Rooms
rom = ["startRoom","room01","room11"]

#[opp,ned,høyre,venstre]
startRoom = Maps([0,0],[0,1,2,3])
room01 = Maps([0,1],[3,4])
room11 = Maps([1,1],[4])

def start():
    print(Start)


def movement():
        retningvalg = []
        romRN = ""

        for i in range(0,len(rom)-1):
            if eval(rom[i]).mapPosition == player.position :
                retningvalg = eval(rom[i]).retninger
                romRN = rom[i]
        
        validInput = False


        while validInput == False:
            print("\n\nDu står i",romRN,"\n\t0 = Opp \n\t1 = Ned \n\t2 = Høyre\n\t3 = Venstre \n\nDine valg er: ",retningvalg)
            retningInput= input("Skriv inn tallet til ønsket retning:")

            for i in range(0,len(retningvalg)):
                try:
                    if int(retningInput) == retningvalg[i]:
                        validInput = True          
                except:
                    print("feil")

        retningInput = int(retningInput)
            
        if retningInput == 0:
            player.position[1] += 1
        elif retningInput == 1:
            player.position[1] -= 1
        elif retningInput == 2:
            player.position[0] += 1
        elif retningInput == 3:
            player.position[0] -= 1
 

        print(player.position)

        return player.position

def fight():
    def heal():
        player.hp += 10
        return player.hp
    
    def angrip():
        boss.hp -= 10
        return boss.hp
    
    print("Ånei!!!! Der var det en Boss!!!! \n\nDine valg er: \n\n\t1 = Heal \n\t2 = Angrip")
    svar = int(input("Hva velger du?"))

    if svar == 1:
        heal()
    elif svar ==2:
        angrip()

    

        

# Intro

# start()
movement()
# fight()

