# https://ioflood.com/blog/python-write-to-csv/
# Python Write to CSV | Guide (With Examples). (u.å.). Hentet 18. april 2024, fra https://ioflood.com/blog/python-write-to-csv/ - («Python Write to CSV | Guide (With Examples)», u.å.)

import csv
import pandas as pd
import os

# with open('file.csv', 'w', newline='') as file:  
#     writer = csv.writer(file)
#     # writer.writerow(['linenumber','datetime','athlete','distance','duration','gender','age_group','country','major'])

import csv

# with open('file.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'age'])
#     writer.writerow(['John Doe', 30])

# Output:
# The CSV file named 'file.csv' will be created and two rows of data will be written to it.



def absRef(relRef):
   return os.path.join(os.path.dirname(__file__), relRef) #Lånt av linus

df = pd.read_csv(absRef("run_ww_2020_w-PROVE.csv"))


  
with open('male.csv', 'w', newline='',encoding= 'utf-8') as file:  
    writer = csv.writer(file)
    writer.writerow(['linenumber','datetime','athlete','distance','duration','gender','age_group','country','major'])
    for i in range(0,30):
        if df["gender"][i] == "M":
            writer.writerow([df['linenumber'][i],df['datetime'][i],df['athlete'][i],df['distance'][i],df['duration'][i],df['gender'][i],df['age_group'][i],df['country'][i],df['major'][i]])

with open('female.csv', 'w', newline='',encoding= 'utf-8') as file:  
    writer = csv.writer(file)
    writer.writerow(['linenumber','datetime','athlete','distance','duration','gender','age_group','country','major'])
    for i in range(0,30):
        if df["gender"][i] == "F":
            writer.writerow([df['linenumber'][i],df['datetime'][i],df['athlete'][i],df['distance'][i],df['duration'][i],df['gender'][i],df['age_group'][i],df['country'][i],df['major'][i]])