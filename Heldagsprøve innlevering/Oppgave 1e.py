import osmnx as ox
import folium as fol
import os
import csv

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Lånt av linus

filnavn = absRef("utleige.csv")   

# # Byenes koordinater
# punkter = [
#   [59.9139, 10.7522],  # Oslo
#   [55.6761, 12.5683],  # København
#   [59.3293, 18.0686]   # Stockholm
# ]

stedsnavn = []
topStedsnavn = []
reviews = []
topReviews = []

with open(filnavn, encoding="utf-8-sig") as fil:  ### Hentet fra læreboken
    filinnhold = csv.reader(fil, delimiter=",")

    for rad in filinnhold:
        if rad[1] not in stedsnavn:
            stedsnavn.append(rad[1])
            reviews.append(rad[11])



reviews,stedsnavn = zip(*sorted(zip(reviews, stedsnavn))) #https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other

print(reviews)
def sort_list(list1, list2):
 
    zipped_pairs = zip(list2, list1)
 
    z = [x for _, x in sorted(zipped_pairs)]  #https://www.geeksforgeeks.org/python-sort-values-first-list-using-second-list/
 
    return z

# print(sort_list(reviews,stedsnavn))

for i in range(0,len(reviews)-1):
    if reviews[i].isnumeric() == True:
        reviews[i]= float(reviews[i])

zdgh = zip(*sorted(zip(stedsnavn, reviews)))

print(zdgh)
print(reviews)

topSted = [stedsnavn[len(stedsnavn)-1],stedsnavn[len(stedsnavn)-2],stedsnavn[len(stedsnavn)-3],stedsnavn[len(stedsnavn)-4],stedsnavn[len(stedsnavn)-5]]
topReviews = [reviews[len(reviews)-1],reviews[len(reviews)-2],reviews[len(reviews)-3],reviews[len(reviews)-4],reviews[len(reviews)-5]]

  

# print(topReviews)

# bredde_sum = 0
# lengde_sum = 0

# for punkt in punkter:
#   bredde_sum += punkt[0]
#   lengde_sum += punkt[1]

# bredde_snitt = bredde_sum / len(punkter)
# lengde_snitt = lengde_sum / len(punkter)

# # Lager et kart
# m = fol.Map([bredde_snitt, lengde_snitt], zoom_start=6) ## hentet fra boken fikk ikke tid til å gjøre dette. Sorteringen av listene knotet seg til

# # Legger til byene
# for punkt in punkter:
#   fol.CircleMarker(punkt).add_to(m)

# # Lagrer kartet
# m.save("skandinavia.html")