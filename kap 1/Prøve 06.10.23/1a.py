lengde = float(input("Skriv lengden på bildet (Antall pixler)"))
bredde = float(input("Skriv bredden på bilder (Antall pixler)"))

if bredde//lengde < 1:
    print("Portrait")
elif lengde//bredde <= 1:
    print("landscape")