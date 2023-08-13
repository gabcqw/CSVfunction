import os
import sys
import csv 
import pickle
import json

class WrongNumOfCellInRowErr(Exception):
    pass

class InsufficientDataErr(Exception):
    pass

class FileTypeNotFoundERR(Exception):
    pass

def validat_data(content):

    for idx, row in enumerate(content):
        if len(row) != 4: #create wrong data doc to test
            raise WrongNumOfCellInRowErr(f"Incorrect number of cells in row: {idx} {row}. /n")
        
    if len(row) < 4:
        raise InsufficientDataErr(f"Only {len(content)- 1} rows. Please enter more date if you wish. /n")

def reader_csv(file_name):
    data = []
    
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        
    return data


class FileHandler:
    PKG_attr = None
    def read(self, file_name):
        with open(file_name, "rb") as f:
            return self.PKG_attr.load(f)
    def write(self, content, file_name):
        with open(file_name, "wb") as f:
            return self.PKG_attr.dump(content, f)
        
class JSHandler:
    PKG_attr = json
    

class CSVHandler:
    PKG_attr = pickle
    
    def write(self, content, file_name):
        with open(file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(content)
            
class PKLHandler:
    def read(self, file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    def write(self, content, file_name):
        with open(file_name, "wb") as f:
            return pickle.dump(content, f)


#need header? need zip function?
def csv_to_list_dicts(content):
    rows = content[1:]
    return [dict(zip(row)) for row in rows]

class DataProcessor:
    def __init__(self, in_file, out_file):
        self.in_file=in_file
        self.out_file=out_file
        self.input_handler= None
        self.output_handler= None
    
    def get_hdlr_for_files(self, file_name):
        if file_name.endwith(".csv"):
            return CSVHandler
        elif file_name.endwith(".json"):
            return JSHandler
        elif file_name.endwith(".pkl"):
            return PKLHandler
        else: 
            raise FileTypeNotFoundERR(f"{file_name}- this document type is not supported. /n")
    
    def update_processor(self):
        self.input_handler = self.get_hdlr_for_files(self.in_file)
        self.oput_handler = self.get_hdlr_for_files(self.out_file)
    
    def read_content(self):
        self.content = self.input_handler(self.in_file)
    
    def write_content(self):
        self.output_handler.write(self.out_file)

#QQ? the modify part equals changes part in reader py?
    def modify_content(self):
        output = []
        for content in content:
            col = int(content.split(',')[0])
            row = int(content.split(',')[1])
            value = content.split(',')[2]
            if row < len(output) and col < len(output[row]):
                output[row][col] = value
            else:
                print(f"Warning: Ignoring update '{output}' - Invalid row or column.")
            output.append(row)
            output.append(col) 
            self.content = output
            

    def run(self):
        self.update_processor()
        self.read_content()
        self.write_content()
        self.modify_content()



if __name__ == "_main_":
    if not len(sys.argv) >1:
        print(f"ERROR: You should enter more arguments: {sys.argv}")
        exit()

content = reader_csv("in.csv")
for row in content[:4]:
    print(row)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        all_file = os.path.spilt(file_path)[0]
        if not all_file:
            all_file = os.getcwd()
        other_files = [
            f for f in os.listdir(all_file)
            if not os.path.isdir(f) and (".csv" in f or ".json" in f or ". pkl" in f)
        ]
        print("ERROR: It does not exist: {file_path}")
        print("Do you mean to find one of these files: {other_files}?")
        exit()
    
#检查是否需要
#file_reader = get_hdlr_for_files(file_path)
    #print(file_reader)
        #exit()


    content = reader_csv(file_path)

    try:
        validat_data(content)
    except WrongNumOfCellInRowErr as e:
        print(f"ERROR: {e}")
        exit()

    except InsufficientDataErr as e:
        print(f"WARNING: {e}")
        exit()

#周一测试这个的时候可以看一下是否通过，不可以的话删掉 pkl json 
#jh=JSHandler, jh.save(content, "update_json.json")
    with open("Indata.json", "w") as f:
        json.dump(content, f, indent = 1)
    
    with open("Indata.pkl", "wb") as f:
        json.dump(content, f)

    content = csv_to_list_dicts(content)
    



    