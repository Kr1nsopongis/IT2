import random as r
tall = 0
streak = 0

print("Stein, saks ,papir!! Spillet fortsetter til du klarer å vinne tre ganger på rad")

while streak < 3:
    
    poeng = 0
    streak = 0
    tall = int(r.randint(1,3))
    brukerInp = input("Skriv 'stein' 'saks' eller 'papir'")
    if brukerInp == "stein":
        poeng = 1
    elif brukerInp == "saks":
        poeng = 2
    elif brukerInp == "papir":
        poeng = 3

    print(poeng)
    print(tall)

    if poeng == 1 and tall == 2:
        print("du vant")
        streak = streak + 1
    elif poeng == 2 and tall == 3:
        print("du vant")
        streak = streak + 1
    elif poeng == 3 and tall == 1:
        print("du vant")
        streak = streak + 1
    elif poeng == tall:
        print("uavgjort")
    else:
        print("datamaskinen vant")
#while-løkke som kjører helt til spilleren har vunnet tre ganger. 
if streak == 3:
        print("du vant tre ganger")
    
    