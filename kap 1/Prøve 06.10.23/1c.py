import datetime
tid = datetime.datetime.now()   #kilde: https://www.geeksforgeeks.org/get-current-date-using-python/
detteÅr = str(tid.year)

fødselsNr = input("Skriv et fødselsnummer")
måneder = ["januar","februar", "mars", "april", "mai","juni","juli","august","september","oktober","november","desember"]
datoIMåned = int(fødselsNr[0])*10 + int(fødselsNr[1])
måned = int(fødselsNr[2])*10 + int(fødselsNr[3])
månedTxt = "" '''Lagt til i etterkant'''
år = int(fødselsNr[4])*10 + int(fødselsNr[5])
kjønn = ""

# if måned == 1:
#     månedTxt = "Januar"
# elif måned == 2:
#     månedTxt = "Februar"
# elif måned == 3:
#     månedTxt = "Mars"
# elif måned == 4:
#     månedTxt = "April"
# elif måned == 5:
#     månedTxt = "Mai"
# elif måned == 6:                  ##### lagt til i etterkant 
#     månedTxt = "Juni"
# elif måned == 7:
#     månedTxt = "Juli"
# elif måned == 8:
#     månedTxt = "August"
# elif måned == 9:
#     månedTxt = "September"
# elif måned == 10:
#     månedTxt = "Oktober"
# elif måned == 11:
#     månedTxt = "November"
# elif måned == 12:
#     månedTxt = "Desember"



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
    # print(f"Fødselsdatoen er {datoIMåned}.{månedTxt} {år} ({kjønn})") Andre mulighet. dette er lagt til i ettertid
else:
    print("Fødselsnummeret må være 11 siffer langt. prøv på nytt")
    
    
