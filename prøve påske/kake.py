import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

pd.set_option('display.max_rows', None)

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Stjelt av linus

filnavn = absRef("run_ww_2020_w-PROVE.csv")

liste = []
tall = []

df = pd.read_csv(filnavn)

for i in range(0,len(df)):
   if df['age_group'][i] not in liste:
      liste.append(df['age_group'][i])
      tall.append(1)
   else:
      tall[liste.index(df['age_group'][i])] += 1



print(tall)

for i in range(0,len(liste)):
   print(liste[i],"--",tall[i])


x = liste
y = tall
plt.pie(y, labels= y)
plt.title("Aldersfordeling")
plt.show()  