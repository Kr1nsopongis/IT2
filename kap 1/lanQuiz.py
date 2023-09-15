import random 
landInfo = {
    # key: land [1] = hovedstad [2] = antall land det grenser til
    "Norge" : ["oslo","3"],
    "Sverige" : ["Stocholm","3"],
    "Finland" : ["Helsinki","3"],
    "Island" : ["Reykjavik", "0"]
}

liste = ["Norge","Sverige","Island","Finland"]

a = random.randint(0,len(liste)) - 1

print("Hva er hovedstaden i", liste[a],"?")
skrevetHovedstad = input("skriv her : ")
land = liste[a]

if landInfo[land][0] == skrevetHovedstad:
    print("Du har rett")
else:
    print("Du skrev feil")


print("Hvor mange land tror du ",land," grenser til?")
skrevetGrenseland = input("skriv her: ")

if landInfo[land][1] == skrevetGrenseland:
    print("Du gjettet riktig")
else:
    print("du gjettet feil")
