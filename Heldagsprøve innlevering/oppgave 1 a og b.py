# ---------  Del A ---------
# Det er mange utfordringer en kan støtepå når man skal behandle data fra store datasett. 
# Det første problemet man gjerne møter på er en encodingsfeil eller at csv-readeren ikke klarer å lese enkelte etegn som står skrevet i csven. 
# I dette datasettet finner vi det for eksempel i linje nr: 125053. Her ser vi tegnet: ⚡ I navnet.
#  Uten å ha prøvd å printe dette ut til terminalen er dette noe jeg tenker på som en utfordring
# Dette henger sammen med neste utfordring. En vil jo at programmet skal kjøre gjennopm hele filen for å kunne lage statistikk som har rot i virkelighet.
# Dette er veldig krevende for maskinen. Derfor velger man ofte å kjøre det i en slags "proxy" hvor man bare går i gjennom de første for eksempel 30 linjene.
# Alt kan se bra ut i de første linjene, men når en skal utvide koden til å gå gjennom hele csven kan problemene begynne å komme. 
# Som jeg oppdaget i Del b er ikke alltid dataen som blir lagt inn skjekket for for eksempel at det er skrevet tall og ikke bokstaver her er det lett å møte på utfordringer


import os

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Lånt av linus

import csv

filnavn = absRef("utleige.csv")   

priser = []
riktigePriser = []

with open(filnavn, encoding="utf-8-sig") as fil:  ### Hentet fra læreboken
  filinnhold = csv.reader(fil, delimiter=",")

  for rad in filinnhold:
    if rad[9].isnumeric() == True: ## https://www.w3schools.com/python/ref_string_isnumeric.asp
        priser.append(rad[9])



for i in range(0,len(priser)):
   
   priser[i] = int(priser[i])   
   if priser[i] != 0:
      riktigePriser.append(priser[i]) # Fjerer prisene som er opgitt som 0 da dette ikke er troverdig.

dyrest = max(riktigePriser)
billigst = min(riktigePriser)
gjennomsnitt = sum((riktigePriser))/len(riktigePriser)


print(f"Dyreste boligen koster {dyrest} dollar for ett døgn. Billigste koster {billigst} dollar for ett døgn. Gjennomsnittet er {gjennomsnitt} dollar for ett døgn") #Det virket først urimelig med 9999$ for en natt men etter å ha søkt gjennom datasettet fant jeg ut at alle de respektive leilighetene med den prisen var plassert på manhatten, verdens dyreste boligstrøk. Derfor ser jeg på det som sannsynlig at det kan stemme. 




