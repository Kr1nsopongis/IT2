lengde = input("Skriv lengden på bildet (Antall pixler)")
bredde = input("Skriv bredden på bilder (Antall pixler)")

if lengde*0 == 0:
    lengde = float(lengde)
else:
    print("Du må skrive et tall!!")

if bredde*0 == 0:
    bredde = float(bredde)
else:
    print("Du må skrive et tall!!")

if bredde/lengde < 1:
    print("Portrait")
elif lengde/bredde < 1:
    print("landscape")
elif lengde/bredde == 1:
    print("kvadrat")

