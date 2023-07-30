import os
import sys
import csv 



print()
#check if the document exists 

in_file =sys.argv[1] 
out_file = sys.argv[2]
changes = sys.argv[3:]
print(changes)
file_exists = os.path.exists(in_file)
print(f"{in_file} exists?", file_exists,"\nTrue, continue. False, you need to try enter the other file name.\n")


files_in_folder = os.listdir()

#read the csv file
print(f"\nLet's make some changes in {in_file}: \n")

data = []

try:
    with open(in_file, "r") as f:
        reader = csv.reader(f)
    for line in reader:
        data.append(line)
except FileNotFoundError:
     print("This file does not exist.")
     print("Current files inside the folder are: \n")
     for file in files_in_folder:
        print(file)

#use collum index and rox index- change value 1,1,cat
try:
    with open(out_file, "w", newline="") as f:
        writer= csv.writer(f)
    for row in data:
        writer.writerow(row)
        for change in changes:
            print (change.split(","))
except FileNotFoundError:
     print("Failed to run the command.")

csv_data = csv.reader(f)
for change in changes:
        try:
            col, row, value = map(int, change.split(','))
            if row < len(csv_data) and col < len(csv_data[row]):
                csv_data[row][col] = value
            else:
                print(f"Warning: Ignoring update '{change}' - Invalid row or column.")
        except ValueError:
            print(f"Warning: Ignoring invalid update '{change}' - Incorrect format.")

print(sys.argv)
print()
print ("Arguement 3", sys.argv[3:])

if len(sys.argv) >4:
    print("Arguement 5:", sys.argv[5])
else:
    print("There is no 5th argument in the list.")

print("Please check contents inside out.csv.")


