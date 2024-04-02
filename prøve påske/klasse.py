import pandas as pd
import matplotlib.pyplot as plt
import os


def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Stjelt av linus

filnavn = absRef("run_ww_2020_w-PROVE.csv")


df = pd.read_csv(filnavn)
liste = []
tall = []

for i in range(0,len(df)):
   if df['age_group'][i] not in liste:
    liste.append(['age_group'][i])
    tall.append(1)
    print(liste)
    
   else: 
    tall[liste.index(df['gender'][i]+df['age_group'][i])] +=1

for i in range(0,len(liste)):
   print(liste[i],"--",tall[i])

x = liste
y = tall
plt.pie(y, labels= x)
plt.title("Aldersfordeling")
plt.show()

