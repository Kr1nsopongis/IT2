# tall = []

# for i in range(1,6):    
#     tall.append(i**2)

# print(tall)
i= 0
dager = ["Mandag","Tirsdag","Onsdag","Torsdag","Fredag","lørdag","Søndag"]
nedbør = []
temperatur = []
vindstyrke = []

for i in range (0,7):
    regn = float(input (f"Hvor mange millimeter nedbør var det på på {dager[i]}?\t:"))
    temp = float(input(f"Hva var temperaturen på {dager[i]}?\t\t\t:"))
    vind = float(input(f"Hva var vindstyrken på {dager[i]}?\t\t\t\t:"))
    nedbør.append(regn)
    temperatur.append(temp)
    vindstyrke.append(vind)
    print(nedbør)
    print(temperatur)
    print(vindstyrke)

høyestRegn = max(nedbør)
print(høyestRegn)

print("På",dager[nedbør.index(høyestRegn)],"var det høyest mengde nedbør med",høyestRegn,"mm på 24 timer!")
print("Det regnet i gjennomsnitt: ",sum(nedbør)/len(nedbør),"mm hver dag")
print("Det var i gjennomsnitt: ",sum(temperatur)/len(temperatur),"grader celcius")
print("Det blåste i gjennomsnitt: ",sum(vindstyrke)/len(vindstyrke),"m/s hver dag")

