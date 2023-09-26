omgjøringsverdi = 3.6
fart = 0
strekning = 0
tid = 0

def main():
    strekning = input("Skriv inn hvor lang strekningen er")
    global tid
    tid = input("Hvor lang tid du på strekningen i sekunder")
    print(tid)
    speedFromTime()
    speedCheck()

def speedFromTime(): 
    global fart
    print(tid)
    fart = float(strekning)/float(tid)
    print("du kjørte med en gjennomsnitlig fart på",fart,"meter i sekundet")
def speedCheck(): 
    global fart
    fart = fart/omgjøringsverdi
    if fart <= 80: 
        print(" du kjørte i 80 eller mer km/h")
    else:
        print("du kjørte ikke i 80 km/h")

main()

