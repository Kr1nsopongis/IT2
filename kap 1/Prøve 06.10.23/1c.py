import datetime
tid = datetime.datetime.now()   #kilde: https://www.geeksforgeeks.org/get-current-date-using-python/
detteÅr = str(tid.year)

fødselsNr = input("Skriv et fødselsnummer")
måneder = ["januar","februar", "mars", "april", "mai","juni","juli","august","september","oktober","november","desember"]
datoIMåned = int(fødselsNr[0])*10 + int(fødselsNr[1])
måned = int(fødselsNr[2])*10 + int(fødselsNr[3])
år = int(fødselsNr[4])*10 + int(fødselsNr[5])
kjønn = ""

if år > int(detteÅr[2])*10 + int(detteÅr[3]):
    år = 1900+år
else:
    år = 2000+år

if int(fødselsNr[8]) % 2 == 0:
    kjønn = "kvinne"
else:
    kjønn = "mann"


if len(fødselsNr) == 11:
    print(f"{fødselsNr[0]}{fødselsNr[1]}.{fødselsNr[2]}{fødselsNr[3]}.{fødselsNr[4]}{fødselsNr[5]}")
    print(f"Fødselsdatoen er {datoIMåned}.{måneder[måned-1]} {år} ({kjønn})")
else:
    print("Fødselsnummeret må være 11 siffer langt. prøv på nytt")
    
    
