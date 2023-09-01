# tall = []

# for i in range(1,6):    
#     tall.append(i**2)

# print(tall)
i= 0
dager = ["Mandag","Tirsdag","Onsdag","Torsdag","Fredag","lørdag","Søndag"]
nedbør = []
temperatur = []
vindstyrke = []

for i in range (1,8):
    regn = input("Hvor mange millimeter nedbør var det denne dagen")
    temp = input("Hva var temperaturen denne dagen?")
    vind = input("Hva var vindstyrken denne dagen?")
    nedbør.append(regn)
    temperatur.append(temp)
    vindstyrke.append(vind)
    print(nedbør)
    print(temperatur)
    print(vindstyrke)