import os 
import csv

stations = []

### GENERAL FUNCTIONS ###

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) # Finds right path

dataFrame = absRef("weatherStations.csv")

### CLASSES ###
class WeatherStation:
    def __init__(self,name, positionX, positionY):
        self.name = name
        self.positionX = positionX
        self.positionY = positionY
    
    def selfInfo(self):
      print("Information: ","\n\tStation name: ",self.name,"\n\tNo further information")
    
    def selfPos(self):
       print("The station is located at: \n\tX: ",self.positionX, "\n\tY: ",self.positionY)

class RadonStation(WeatherStation):
   def __init__(self, name, positionX, positionY,radonLevel):
      super().__init__(name, positionX, positionY)
      self.radonLevel = radonLevel

   def selfInfo(self):
      print("Information: ","\n\tStation name: ",self.name,"\n\tRadon level: ",self.radonLevel)

class PressureStation(WeatherStation):
  def __init__(self, name, positionX, positionY,pressure):
    super().__init__(name, positionX, positionY)
    self.pressure = pressure 
  
  def selfInfo(self):
    print("Information: \n\t","Name: ",self.name,"\n\t Pressure: ",self.pressure)

  
with open (absRef("weatherStations.csv"), 'r', newline='',encoding= 'utf-8') as file:
  reader = csv.reader(file, delimiter=",")
#   writer = csv.writer(file)
  for row in reader: # Retreives stations from CSV and adds to list 
    
    if row[3] != "NaN":
      stations.append(RadonStation(row[0],row[1],row[2],row[3]))
    else:
      stations.append(WeatherStation(row[0],row[1],row[2]))

def updateDF():
   with open (absRef("weatherStations.csv"), 'w', newline='',encoding= 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name','positionX','positionY','radonLevel','pressure','moisture','wind'])   

    for i in range(1,len(stations)):
      try:
        try:
          if stations[i].radonLevel != "NaN":
            writer.writerow([stations[i].name,stations[i].positionX,stations[i].positionY,stations[i].radonLevel],"NaN")
            print("skrivrad")
        except:
          if stations[i].pressure != "NaN":
            writer.writerow([stations[i].name, stations[i].positionX, stations[i].positionY, "NaN", stations[i].pressure, "NaN", "NaN"])
            print("skrivtrykkj")
      except:
        writer.writerow([stations[i].name,stations[i].positionX,stations[i].positionY,"NaN","NaN","NaN","NaN"])
        print("skrivalt")        

def addStation():
    print("Fill in information about station. If no info put in: NaN")
    name = input("Name of station?")
    positionX = input("Position X?")
    positionY = input("Position Y?")
    radonLevel = input("Radon level?")
    pressure = input("Pressure?")
    if radonLevel != "NaN":
      stations.append(RadonStation(name,positionX,positionY,radonLevel))
    elif pressure != "NaN":
      stations.append(PressureStation(name,positionX,positionY,pressure))
      print("Lager pressure")
    else:
      stations.append(WeatherStation(name,positionX,positionY))

    updateDF()
  
def RemoveStation():
  removeName = input("Write the name of the station you want to remove")
  for i in range(1,len(stations)):
    if stations[i].name == removeName:
      stations.pop(i)
  updateDF()

# def displayData(choice):
#   choice = str(choice)
#   for i in range(1,len(stations)):
#     if choice == "radonLevel":
#       try:
#         RadonStation.selfInfo()
#       except:
#         pass
#     if choice == "pressure":
#       try:
#         PressureStation.selfInfo()
#       except:
#         pass    
  

status = True
while status:

  print("\nWhat do you want to do?")
  inpt = input("View info of all stations = 1, Add station = 2, Veiw all stations position = 3, Remove station = 4, View all stations with attribute = 5 --->: ")  #Legg inn skjekk

  try: 
    inpt = int(inpt)
    if inpt == 1:
      for i in range(1,len(stations)):
        print(stations[i].selfInfo())
    if inpt == 2:
      addStation()
    if inpt == 3:
      for i in range(0,len(stations)):
        print(stations[i].selfPos())
    if inpt == 4:
      RemoveStation()
    if inpt == 5:

      choice = input("Get all stations with either: radonLevel,pressure.\n Write one of the above:  ")
      for station in stations:
        if hasattr(station, choice) and getattr(station, choice) != "NaN": #https://www.codingem.com/python-check-if-object-has-attribute/
            station.selfInfo()
   
  except:
    print("Write one of the following numbers to trigger actions")

