ord = {}
utskrift = {}

def gjette() :
    
    global utskrift
    gjettetBokstav = input("Gjett en bokstav")
    for i in range (0,len(ord)):
        if gjettetBokstav == ord[i]:
            utskrift[i] = gjettetBokstav
    print(utskrift)

def registrerOrd():
    global utskrift
    inputOrd = input("skriv et ord med små bokstaver ")
    i = 0 
    for i in range (0,len(inputOrd)):
        utskrift[i] = "_"
        ord[i] = inputOrd[i]
    print(utskrift)    
  
    print(ord)
    for i in range(0,24):
        gjette()
        if ord == utskrift:
            print("du vant")

registrerOrd()

