varer = {
    "Asus Zenbook GH215": { 
        "pris" : 9999,
        "varelager" : 10,
        "produktinfo" : "En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD",
        "tekniskeEgenskaper" : {
                "prosessor": "Intel Core i5-1135G7",
                "grafikkort": "Intel Iris Xe Graphics",
                "batterikapasitet": "Opptil 8 timer",
                "vekt": "1.8kg",
            },
        "farger": ["svart","blå"]
    },
    "Samsung Galaxy S22 GH67" : {
        "pris": 6999,
        "varelager": 20,
        "produktinfo": "En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera",
        "tekniskeEgenskaper": {
            "prosessor": "Qualcomm Snapdragon 888",
            "grafikkort": "Adreno 600",
            "batterikapasitet": "4500 mAh",
            "vekt": "200g",
        },
        "farger": ["svart","hvit","grønn"]
    },

}

def printVarer():
    print("Vare id: Asus Zenbook GH215 \nPris:", varer["Asus Zenbook GH215"]["pris"],"\nVarelager:",varer["Asus Zenbook GH215"]["varelager"],"\nProduktinfo",varer["Asus Zenbook GH215"]["produktinfo"],"\nTekniske egenskaper:\n","\t - Prosessor:", varer["Asus Zenbook GH215"]["tekniskeEgenskaper"]["prosessor"],"\n\t - Grafikkort",varer["Asus Zenbook GH215"]["tekniskeEgenskaper"]["grafikkort"],"\n\t - Batterikapasitet",varer["Asus Zenbook GH215"]["tekniskeEgenskaper"]["batterikapasitet"],"\n\t - Vekt",varer["Asus Zenbook GH215"]["tekniskeEgenskaper"]["vekt"],"\n Farger:","\n\t -", varer["Asus Zenbook GH215"]["farger"][0],"\n\t -", varer["Asus Zenbook GH215"]["farger"][1],"\n\n")
    print("Vare id: Samsung Galaxy S22 GH67 \nPris:", varer["Samsung Galaxy S22 GH67"]["pris"],"\nVarelager:",varer["Samsung Galaxy S22 GH67"]["varelager"],"\nProduktinfo",varer["Samsung Galaxy S22 GH67"]["produktinfo"],"\nTekniske egenskaper:\n","\t - Prosessor:", varer["Samsung Galaxy S22 GH67"]["tekniskeEgenskaper"]["prosessor"],"\n\t - Grafikkort",varer["Samsung Galaxy S22 GH67"]["tekniskeEgenskaper"]["grafikkort"],"\n\t - Batterikapasitet",varer["Samsung Galaxy S22 GH67"]["tekniskeEgenskaper"]["batterikapasitet"],"\n\t - Vekt",varer["Samsung Galaxy S22 GH67"]["tekniskeEgenskaper"]["vekt"],"\n Farger:","\n\t -", varer["Samsung Galaxy S22 GH67"]["farger"][0],"\n\t -", varer["Samsung Galaxy S22 GH67"]["farger"][1],"\n\t -", varer["Samsung Galaxy S22 GH67"]["farger"][2])

def oppdaterePris():
    id = input("Skriv inn en vare ID")
    nyPris = input("skriv inn den nye prisen")
    varer[id].update({"pris":nyPris})  #https://www.tutorialspoint.com/How-to-update-a-Python-dictionary-values

def oppdatereFarge():
    id = input("Skriv inn en vare ID")
    nyFarge = input("skriv inn den nye fargen")
    varer[str(id)]["farger"].append(nyFarge)  #https://www.geeksforgeeks.org/appending-to-list-in-python-dictionary/

oppdatereFarge()
# oppdaterePris()
printVarer()

#Ble ikke feerdig med denne men føleer jeg fikk gjort en del likevel