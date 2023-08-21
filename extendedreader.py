import os
import sys
import csv 
import pickle
import json

##select functions: reader, change, save 

#Reader functions 
def reader_csv(file_name):
    data = []
    
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def reader_json(file_name):
    with open(file_name, "rb") as f:
        data = json.load(f)
    
    return data

def read_pickle(file_name):
    with open(file_name, "rb") as f:
        data= pickle.load(f)

    return data

def modify_content(content_file, changes):
        for change in changes:
            col = int(change.split(',')[0])
            row = int(change.split(',')[1])
            value = change.split(',')[2]
            if row < len(content_file) and col < len(content_file[row]):
                content_file[row][col] = value
            else:
                print(f"Warning: Ignoring update '{content_file}' - Invalid row or column.")
        
        return content_file

def save_json(output_file_name, changed_content):
        with open(output_file_name, "wb") as f:
            json.dump(changed_content, f)
        
    
def write(output_file_name, changed_content):
        with open(output_file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(changed_content)
            
def write(output_file_name, changed_content):
        with open(output_file_name, "wb") as f:
            return pickle.dump(changed_content, f)


if __name__ == "_main_":

    # Add validation of input

    # Get variables
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    changes = sys.argv[3:]
    
    class CsvHandler:
        def read(self, file_name):
            data = []

            with open(file_name, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    data.append(row)

            return data

        def write(self, file_name, content):
            with open(file_name, "w", endline="") as f:
                writer = csv.writer(f)
                writer.writerows(content)

    class PklHandler:
        def read(self, file_name):
            with open(file_name, "rb") as f:
             return pickle.load(f)
        def write(self, content, file_name):
            with open(file_name, "wb") as f:
                return pickle.dump(content, f)
            
    class JsonHandler:
        def read(self, file_name):
            with open(file_name, "rb") as f:
                return json.load(f)
        def write(self, content, file_name):
            with open(file_name, "wb") as f:
                return json.dump(content, f)



    def select_handler(file_name):
        if file_name.endswith(".csv"):
            return CsvHandler()
        elif file_name.endswith(".json"):
            return JsonHandler()
        elif file_name.endswith(".pickle"):
           return PklHandler()
        else:
            raise Exception(f"File type not supported: {input_file_name}")

    if not os.path.exists(input_file_name):
        all_file = os.path.spilt(input_file_name)[0]
        if not all_file:
            all_file = os.getcwd()
        other_files = [
            f for f in os.listdir(all_file)
            if not os.path.isdir(f) and (".csv" in f or ".json" in f or ". pkl" in f)
        ]
    
    file = select_handler(input_file_name)
    data1 = file.read(input_file_name)
    print(data1)
 



    