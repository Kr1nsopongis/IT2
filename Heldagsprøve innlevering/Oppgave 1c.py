import matplotlib.pyplot as plt
import os

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Lånt av linus

import csv

filnavn = absRef("utleige.csv")   

hostId = []
antallUtleieenheter = []


with open(filnavn, encoding="utf-8-sig") as fil:  ### Hentet fra læreboken
    filinnhold = csv.reader(fil, delimiter=",")

    for rad in filinnhold:
        if rad[2] not in hostId:
            hostId.append(rad[2])
            antallUtleieenheter.append(1)
        else:
            antallUtleieenheter[hostId.index(rad[2])] += 1

antallUtleieenheter,hostId = zip(*sorted(zip(antallUtleieenheter, hostId))) #https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other

hostNavn = []
topHost = [hostId[len(hostId)-1],hostId[len(hostId)-2],hostId[len(hostId)-3],hostId[len(hostId)-4],hostId[len(hostId)-5]]
topAntall = [antallUtleieenheter[len(antallUtleieenheter)-1],antallUtleieenheter[len(antallUtleieenheter)-2],antallUtleieenheter[len(antallUtleieenheter)-3],antallUtleieenheter[len(antallUtleieenheter)-4],antallUtleieenheter[len(antallUtleieenheter)-5]]


with open(filnavn, encoding="utf-8-sig") as fil:  ### Hentet fra læreboken
    filinnhold = csv.reader(fil, delimiter=",")

    for rader in filinnhold:
        if rader[3] not in hostNavn:
       
            if rader[2] in topHost:
                print("hei")
                hostNavn.append(rader[3])

topAntall.reverse() #https://www.programiz.com/python-programming/methods/list/reverse#google_vignette

print(hostNavn,topAntall)

x = hostNavn
y = topAntall
plt.bar(x,y)
plt.title("De fem største utleierene")
plt.show()
