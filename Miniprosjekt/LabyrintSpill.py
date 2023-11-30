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
    def __init__(self, mapPosition, retninger,effekt):
        super().__init__(mapPosition, retninger)
        self.effekt 
        

# Players
player = Player([0,0],100,0)
boss = Player([0,1],200,0)

# random.randint(0,10),random.randint(0,10)

# Rooms
rom = ["startRoom","room01","room11"]

#[opp,ned,høyre,venstre]
roomN1N1 = SpecialMaps([-1,-1],[0],"trap")
room0N1 = Maps([0,-1],[0,2])
room1N1 = Maps([1,-1],[1,2,3])
room2N2 = Maps([2,-1],[0,3])

roomN10 = Maps([-1,0],[0,1,2])
startRoom = SpecialMaps([0,0],[0,1,2,3],"weaponSelect")
room10 = Maps([1,0],[0,1,3])
room20 = Maps([2,0],[0,1])

roomN11 = Maps ([-1,1],[0,1,2])
room01 = Maps ([0,1],[1,2,3])
room11 = Maps ([1,1],[1,3])
room21 = Maps ([2,1],[0,1])

roomN12 = Maps ([-1,2],[1,2])
room02 = Maps ([0,2],[2,3])
room12 = SpecialMaps ([1,2],[2,3],"trap")
room22 = Maps ([2,2],[0,1])


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
                    print("")

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
    
    validInput = False 

    while validInput == False:
        print("\n\n\n\nÅnei!!!! Der var det en Boss!!!! \n\nDine valg er: \n\n\t1 = Heal \n\t2 = Angrip")
        svar = input("Hva velger du?")

        alternativer = [1,2]
       
        for i in range(0,len(alternativer)):
                try:
                    if int(svar) == alternativer[i]:
                        validInput = True          
                except:
                    print("")

    if svar == 1:
        heal()
        print("Din gjenværende HP: ",player.hp)
    elif svar ==2:
        angrip()
        print("Bossens gjenværende HP: ",boss.hp)

while player.hp >= 0 and boss.hp >= 0:

    if player.positon == [0,0]:
           

        

# Intro

# start()
# movement()
fight()

