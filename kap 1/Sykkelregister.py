Brukervalg = input("Vil du registrer en ny sykkel       skriv: Ja/Nei")
navn = ""
adresse = ""
navnInp = ""
navnInp = ""

register = {}




def registrer():
    Brukervalg = ""
    rammeNr = input("Skriv inn rammenummeret på sykkelen")
    navnInp = input("hvilket navn skal sykkelen registreres på?")
    adresseInp = input("hvor bor du?")
    
    register[rammeNr] = [
    navnInp , 
    adresseInp
    ]
    Brukervalg = input("Vil du registrer en ny sykkel       skriv: Ja/Nei")

    
if Brukervalg == "Ja":
    registrer()
elif Brukervalg = "Nei"

# registrer()
print(register)