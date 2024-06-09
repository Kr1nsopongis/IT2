import matplotlib.pyplot as plt
import os

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Lånt av linus

import csv

filnavn = absRef("utleige.csv")   

nabolag = []
nabolagTeller = []


with open(filnavn, encoding="utf-8-sig") as fil:  ### Hentet fra læreboken
    filinnhold = csv.reader(fil, delimiter=",")

    for rad in filinnhold:
        if rad[4] not in nabolag:
            nabolag.append(rad[4])
            nabolagTeller.append(1)
        else:
            nabolagTeller[nabolag.index(rad[4])] += 1

print(nabolagTeller)
nabolagTeller,nabolag = zip(*sorted(zip(nabolagTeller, nabolag))) #https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other


topNabolag = [nabolag[len(nabolag)-1],nabolag[len(nabolag)-2],nabolag[len(nabolag)-3],nabolag[len(nabolag)-4],nabolag[len(nabolag)-5]]
topAntall = [nabolagTeller[len(nabolagTeller)-1],nabolagTeller[len(nabolagTeller)-2],nabolagTeller[len(nabolagTeller)-3],nabolagTeller[len(nabolagTeller)-4],nabolagTeller[len(nabolagTeller)-5]]


print(nabolagTeller)
# with open(filnavn, encoding="utf-8-sig") as fil:  ### Hentet fra læreboken
#     filinnhold = csv.reader(fil, delimiter=",")

#     for rader in filinnhold:
#         if rader[4] in topHost:
#             print("hei")
#             hostNavn.append(rader[4])



# print(topNabolag,topAntall)

x = topNabolag
y = topAntall
plt.bar(x,y)
plt.title("De fem største nabolagene")
plt.show()

#### Fikk ikke tid til å gjøre oppgave E