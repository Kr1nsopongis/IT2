import pandas as pd
import matplotlib.pyplot as plt
import os

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) # Finds right path

year = []
yearCount = []

dataFrame = pd.read_csv(absRef("NORGE-RUNDT.csv"),on_bad_lines= 'skip',delimiter=';')

for i in range(0,len(dataFrame)):
   if dataFrame['aar'][i] not in year:
      year.append(dataFrame['aar'][i])
      yearCount.append(1)
   else:
      yearCount[year.index(dataFrame['aar'][i])] += 1

plt.barh(year,yearCount)
plt.show()