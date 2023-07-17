import os
import sys
import csv 

print(sys.argv)
print()
#check if the document exists 
file_search= input("Please enter the file name you want to search: \n")
file_exists = os.path.exists(file_search)
print(f"{file_search} exists?", file_exists,"\nTrue， continue. False，you need to try enter the other file name.\n")

#list the files of the folder

files_in_folder = os.listdir()

print("Current files inside the folder are: \n")
for file in files_in_folder:
    print(file)

#read the csv file
print(f"\nLet's make some changes in {file_search}: \n")

data = []
#from the string to list -value x,y,z, using .split syntax
with open("in.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        data.append(line)

for num, row in enumerate(data):
    if row[0] == "door":
        row[0] = "piano"
    elif row[1] == "1":
        row[1] = "mug"
    elif row[2] == "22":
        row[2] = "17"
    elif row[3] == "stick":
        row[3] = "0"
    

with open("out.csv", "w", newline="") as f:
    writer= csv.writer(f)
    for row in data:
        writer.writerow(row)
print("Please check contents inside out.csv.")

