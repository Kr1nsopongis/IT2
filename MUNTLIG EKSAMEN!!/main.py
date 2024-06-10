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

class PressureStations(WeatherStation):
  def __init__(self, name, positionX, positionY,pressure):
    super().__init__(name, positionX, positionY)
    self.pressure = pressure 
  
    
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
        if stations[i].radonLevel != "NaN":
          writer.writerow([stations[i].name,stations[i].positionX,stations[i].positionY,stations[i].radonLevel])
      except:
        writer.writerow([stations[i].name,stations[i].positionX,stations[i].positionY,])
              

def addStation():
    print("Fill in information about station. If no info put in: NaN")
    name = input("Name of station?")
    positionX = input("Position X?")
    positionY = input("Position Y?")
    radonLevel = input("Radon level?")
    if radonLevel != "NaN":
      stations.append(RadonStation(name,positionX,positionY,radonLevel))
    else:
      stations.append(WeatherStation(name,positionX,positionY))
  
    updateDF()

status = True
while status == True:

  print("\n What do you want to do?")
  inpt = input("View info of one station = 1, Add station = 2, Quit = 3")
  inpt = int(inpt)
  print(type(inpt))
  try: 
    inpt = int(inpt)
    if inpt == 1:
      for i in range(0,len(stations)):
        print(stations[i].selfInfo())
    if inpt == 2:
      addStation()
    if inpt == 3:
      status == False
  except:
    print("Write one of the following numbers to trigger actions")
    # inpt = input("View info of one station = 1, Add station = 2, Quit = 3")
  
