import csv
import pandas as pd
import os
import unittest

def absRef(relRef):

   return os.path.join(os.path.dirname(__file__), relRef) #Lånt av linus

objekter = []
filmer = []
kategorier = []
kategoriVerdi = []

class Objekt:
   def __init__(self,navn,kjopePris,prisVerdi,kategori,franchise):
      self.navn = navn
      self.kjøpePris = kjopePris
      self.prisVerdi = prisVerdi
      self.kategori = kategori
      self.franchise = franchise

   def fortjeneste(self):
      fortjeneste = self.prisVerdi-self.kjøpePris
      print(f"fortjenesten er på {fortjeneste} kroner")

    
class Film(Objekt):
    def __init__(self,navn,kjopePris,prisVerdi,kategori,franchise,varighet):
       super().__init__(navn,kjopePris,prisVerdi,kategori,franchise)
       self.varighet = varighet

class TestLikhet(unittest.TestCase): #https://realpython.com/python-testing/#testing-your-code
   
   def testLikhetObjekt(self):
      self.assertEqual(objekter[0].navn,dataObjekter['navn'][0], "skal være like") # Skjekker at objektene i Csv og Lister ligger samme plass så det ikke forekommer forskyvninger

   def testLikhetFilmer(self):
      self.assertEqual(filmer[0].navn,dataFilmer['navn'][0], "skal være like")

def leggTilObjekt(navn,kjopePris,prisVerdi,kategori,franchise):
    navn = Objekt(navn,kjopePris,prisVerdi,kategori,franchise)
    objekter.append(navn)
    # print(objekter[objekter.index(navn)].navn)

def leggTilFilm(navn,kjopePris,prisVerdi,kategori,franchise,varighet):
    navn = Film(navn,kjopePris,prisVerdi,kategori,franchise,varighet)
    filmer.append(navn)
    # print(filmer[filmer.index(navn)].navn)


#Legg til flere objekter her: 
leggTilObjekt("Fifa 7 ps2",300,35,"spill","Fifa")
leggTilObjekt("Fifa 12 ps3",500,100,"spill","Fifa")
leggTilObjekt("Avengers plakat",100,100,"plakat","Marvel")
leggTilObjekt("Spiderman dukke",150,300,"merchandise","Marvel")
leggTilObjekt("Spiderman drakt",1500,1000,"merchandise","Marvel")
leggTilObjekt("Batmobil",2500000,10000000,"merchandise","DC")

#legg til flere filmer her:
leggTilFilm("Ironman 1",200,100,"film","Marvel",120)
leggTilFilm("Batman",200,100,"film","DC",123)
leggTilFilm("Fifa the movie",200,1,"film","Fifa",456)
leggTilFilm("dfsdf",200,1,"film","djfs",222)

with open (absRef('objekter.csv'), 'w', newline='',encoding= 'utf-8',) as file:
    writer = csv.writer(file)
    writer.writerow(['navn','kjopePris','prisVerdi','kategori','franchise'])
    for objekt in objekter:
       writer.writerow([objekt.navn,objekt.kjøpePris,objekt.prisVerdi,objekt.kategori,objekt.franchise])
    
with open(absRef('filmer.csv'), 'w', newline='',encoding= 'utf-8') as file:  
    writer = csv.writer(file)
    writer.writerow(['navn','kjopePris','prisVerdi','kategori','franchise','varighet'])
    for film in filmer:
       writer.writerow([film.navn,film.kjøpePris,film.prisVerdi,film.kategori,film.franchise,film.varighet])

dataObjekter = pd.read_csv(absRef("objekter.csv")) 
dataFilmer = pd.read_csv(absRef("filmer.csv"))


def utskriftKategori(kategori):
   print(f"I kategorien {kategori} finner vi:\n")
   for rad in range(0,len(dataObjekter)):
    if dataObjekter['kategori'][rad] == kategori:
        print("\t",dataObjekter['navn'][rad])
   for rad in range(0,len(dataFilmer)):
    if dataFilmer['kategori'][rad] == kategori:
        print("\t",dataFilmer['navn'][rad])

def utskriftFranchise(franchise):
   print(f"I franchisen {franchise} finner vi:\n")
   for rad in range(0,len(dataObjekter)):
    if dataObjekter['franchise'][rad] == franchise:
        print("\t",dataObjekter['navn'][rad])
   for rad in range(0,len(dataFilmer)):
    if dataFilmer['franchise'][rad] == franchise:
        print("\t",dataFilmer['navn'][rad])

def fortjenester():
   for objekt in objekter:
      print(objekt.fortjeneste())
   
#Her er funskjonene for å skrive ut ting i de forskjellige kategoriene
utskriftKategori("merchandise")
utskriftKategori("film")
utskriftKategori("spill")
utskriftKategori("plakat")

#Her er funskjonene for å skrive ut ting i de forskjellige franchisene
utskriftFranchise("Marvel")
utskriftFranchise("Fifa")
utskriftFranchise("DC")

if __name__ == '__main__':
    unittest.main()