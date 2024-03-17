import pandas as pd
import matplotlib.pyplot as plt
import os

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Stjelt av linus

data = pd.read_csv(absRef("run_ww_2020_w-PROVE.csv"), delimiter=",", engine= "python")

# print(data.head())

ordbok= []
tall = []

måned = str(data["datetime"])
for rows in data:
   if ordbok.index(måned) == -1:
      ordbok.append(måned)
      tall[ordbok.index(måned)] += 1    
    else

print(ordbok)