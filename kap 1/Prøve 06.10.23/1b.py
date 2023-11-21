liste = []
deleListe = []
i = 1

for i in range(1,101):
    liste.append(i)
    # i = i + 1

print(f"Listen har {len(liste)} elementer")

def heltallsdivisjon():
 
    i = 0
    divisor = 7
    for i in range(0,len(liste)):
        if liste[i] % divisor == 0:
            deleListe.append(liste[i])
    
heltallsdivisjon()

print("Starter søk etter tall som er delelig på 7: ")
for i in range(0,len(deleListe)):
     print(deleListe[i])          

