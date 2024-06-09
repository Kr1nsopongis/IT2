# import csv
import csv
import os
# read csv file to a list of dictionaries

def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Lånt av linus

with open(absRef('Csvdict.csv'), 'r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]



print(data)



