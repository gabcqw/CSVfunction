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

print("Current files inside the folder are: \n")
for file in files_in_folder:
    print(file)

#read the csv file
print(f"\nLet's make some changes in {in_file}: \n")

data = []

with open(in_file, "r") as f:
    reader = csv.reader(f)

    for line in reader:
        data.append(line)

#use collum index and rox index- change value 1,1,cat
for change in changes:
    print (change.split(",")) 
with open(out_file, "w", newline="") as f:
    writer= csv.writer(f)
    for row in data:
        writer.writerow(row)

print(sys.argv)
print()
print ("Arguement 3", sys.argv[3:])

if len(sys.argv) >4:
    print("Arguement 5:", sys.argv[5])
else:
    print("There is no 5th argument in the list.")

print("Please check contents inside out.csv.")


