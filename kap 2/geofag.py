import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


# Les dataene fra filen
data = pd.read_csv(r"kap 2/untitled2.txt" ,skiprows=2, delim_whitespace=True)

# Del dataene i kolonner

time = data["Time"]
light = data["Light"]
temp = data["Temp"]
print("Maksimal lyst effekt", np.max(light))
print("Maksimal lyst effekt", np.min(light))

# Lag en figur med to akser
fig, ax1 = plt.subplots()

# Plot lysnivået på den første aksen med blå farge
ax1.plot(time, light, color="blue", label="Light Level")
ax1.set_ylabel("Light Level")

# Lag en annen akse som deler x-aksen med den første
ax2 = ax1.twinx()

# Plot temperaturen på den andre aksen med rød farge
ax2.plot(time, temp, color="red", label="Temperature")
ax2.set_ylabel("Temperature (°C)")

# Legg til titler og etiketter
plt.title("Måling 4 gråis")
plt.xlabel("Time (s)")
plt.legend("4.Gråis")

# Vis plottet
plt.show()