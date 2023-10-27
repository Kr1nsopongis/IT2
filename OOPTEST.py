# class Planet:
#   def __init__(self, navn, solavstand, radius, antallRinger = 0):
#     self.navn = navn
#     self.solavstand = solavstand
#     self.radius = radius
#     self.antallRinger = antallRinger

# Merkur = Planet("Merkur",1,1)
# Venus = Planet("Venus",2,2)
# Jorda = Planet("Jorda",3,3)

# # print(Merkur.navn)
# # print(Venus.radius)
# # print(Jorda.solavstand)

# class Person:
#   """
#   fjdfjsldjf
#   """
#   def __init__(self, fornavn, etternavn, fødselsdato):
#     self.fornavn = fornavn
#     self.etternavn = etternavn
#     self.fødselsdato = fødselsdato

# person = Person("Marius","Rotseth",210605)

# help(Person)

class Bilett():
    def __init__(self):
        self.mva = 0.12
        self.pris = 20
    
    def beregnePris(self):
        rabattpris = self.pris + (self.pris * self.mva)

class Barnebilett(Bilett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.5
    def beregnPris(self):
        rabattpris = self.pris * self.rabatt
        return rabattpris + (rabattpris * self.mva)
    
print