import pygame
import random 
from ascii import *

class Player(): 
    def __init__(self,name,position,hp,weaponDmg):
        self.name = name
        self.position = position
        self.hp = hp 
        self.weapon = weaponDmg

    def movement(self):
        global retningvalg
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
            self.position[1] += 1
        elif retningInput == 1:
            self.position[1] -= 1
        elif retningInput == 2:
            self.position[0] += 1
        elif retningInput == 3:
            self.position[0] -= 1
 

        print(self.position)

        return self.position
    
    def fight(self,annen):
        def heal():
            self.hp += 10
            if self.hp > 100:
                self.hp = 100
            print(f"Du har nå {self.hp} liv igjen")
            return self.hp
            
        
        def angrip():
            annen.hp -= self.weapon
            print(f"{annen} har nå {annen.hp} igjen")
            return annen.hp
        
        validInput = False 

        while validInput == False:
            print("\n\n\n\nÅnei!!!! Der var det en Boss!!!! \n\nDine valg er: \n\n\t1 = Heal \n\t2 = Angrip")
            svar = input("Hva velger du?")

            alternativer = [1,2]
        
            for i in range(0,len(alternativer)):
                    try:
                        if int(svar) == alternativer[i]:
                            svar = int(svar)
                            validInput = True          
                    except:
                        print("")
        if svar == 1:
            heal()
        elif svar == 2:
            angrip()

    def weaponSelect(self):
        weapon = input("Du kan velge mellom Øks(0) og Sverd(1) hvis ikke har du bare hender")
        weapons = [10,15]
        try:
            self.weapon = weapons[int(weapon)]
        except:
            print("Du har bare henda å sloss med, Du kan komme tilbake til dette rommet hvis det skulle funke dårlig!")


class Maps():
    def __init__(self,mapPosition,retninger):
        self.mapPosition = mapPosition
        self.retninger = retninger
    
class SpecialMaps(Maps):
    def __init__(self, mapPosition, retninger,effekt):
        super().__init__(mapPosition, retninger)
        self.effekt = effekt
        

# Players
player = Player("Spiller",[0,0],100,10)
boss = Player("Boss",[2,0],200,10)

# random.randint(0,10),random.randint(0,10)

# Rooms
rom = [
       "roomN1N1","room0N1","room1N1","room2N1",
       "roomN10","startRoom","room10","room20",
       "roomN11","room01","room11","room21",
       "roomN12","room02","room12","room22"
       ]

#[opp,ned,høyre,venstre]
roomN1N1 = SpecialMaps([-1,-1],[0],"trap")
room0N1 = Maps([0,-1],[0,2])
room1N1 = Maps([1,-1],[0,2,3])
room2N1 = Maps([2,-1],[0,3])

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
room12 = SpecialMaps ([1,2],[2,3],"finish")
room22 = SpecialMaps([2,2],[1,3],"test")


def start():
    print(Start)




# Intro

# player.movement()

# start()

while boss.hp > 0 and player.hp > 0:
    if player.position == boss.position:
        player.fight(boss) 
        break
    
    
    retningvalg = []
    romRN = ""
    effekt = ""

    for i in range(0,len(rom)):
        if eval(rom[i]).mapPosition == player.position :
            retningvalg = eval(rom[i]).retninger
            romRN = rom[i]
            print(romRN)
            try:
                effekt = eval(romRN).effekt
            except:
                effekt = ""
    print(effekt)        

    if effekt == "weaponSelect":
        print("test")
        player.weaponSelect()
    
    player.movement()

    
                

     
    