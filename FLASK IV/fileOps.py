

""" READING A TEXT FILE """
# Open rainbow.txt in append mode
rainbowFile = open("files/rainbow.txt", "r")
out = rainbowFile.read(10)
#print(out) # prints "A rainbow"

outAll = rainbowFile.read() # calling read again continues from where it left off, doesnt start from the top. 
#print(outAll) # next call will be empty because the file is already read

# Read from the beginning with .seek
rainbowFile.seek(0) # restarts from the beginning at the first character (R, at pos 0)
outAllAgain = rainbowFile.read() # reads from char 0 to the end
#print(outAllAgain)

# Read from a line 
rainbowFile.seek(3)
oneLine = rainbowFile.readline() # prints out the line from the 4th character
# print(oneLine)

# Read ALL lines 
rainbowFile.seek(0) # restart 
allLines = rainbowFile.readlines() 
# print(allLines) # prints as a list, each line is an item 
#print(allLines[0]) # prints the first line 

# Open sample_text.txt with write+ mode
st = open("files/sample_text.txt", "w+")


""" WRITING A TEXT FILE """
# create a new text file 
sampleFile = open("files/sample_text_rev.txt", "w") # modes: "w" is write-only mode

# Ask for user input 3 times, adds it as a line to the file 
for i in range(3): 
    # a_name = input("Enter the name of the animal: ") # get user input 
    # sampleFile.write(a_name) # write input in file 
    sampleFile.write("\n") # enter to next line 
#sampleFile.close() # safer to close it, conserves resources. although lines written immediately even without closing
# print("Data is written into the file.") 

# Ask for colours 
colorList = [] 
# for i in range(3): 
    # a_name = input("Enter the name of a color: ") 
    # colorList.append(a_name + '\n') 
#sampleFile.writelines(colorList) 
sampleFile.close() 
# print("Data is written into the file.") 


""" APPENDING A TEXT FILE """

sampleFile_a = open("files/sample_text.txt", "a") # the ONLY difference is you open it for appending rather than writing. if opened with "w", it would rewrite what already exists. 
nameList = [] 
# for i in range(3): # repeats 3x, [0,1,2]
    # a_name = input("Enter the name of someone in your class: ") 
   # nameList.append(a_name + '\n') 
# sampleFile_a.writelines(nameList) 
sampleFile_a.close() 
# print("Data is written into the file.") 


""" READING A JSON FILE """
import json

# Read from file and parse JSON (first method)
jsonFile = open("files/test.json", "r") # read mode 
data = json.load(jsonFile)
# print(data)
# print(type(data)) # a list

# Parse JSON info & turn it into a python object (dictionary) (second method)
json_str = '{"name":"Sabs", "fav_col":"red", "fav_city":"montreal"}'
data_2 = json.loads(json_str) 
# print(data_2)
# print(type(data_2))#converts to a dict

# Read JSON file & turn it into python object
jsonFile = open("files/test.json", "r")
out_all_as_string = jsonFile.read()
data_3 = json.loads(out_all_as_string)  # load s => load string
# print(data_3)
# print(type(data_3[0]))



""" WRITING JSON """
# Using json.dumps() to turn python dict into json obj, then write it into the file 
data_toSave = {"name":"mandy", "fav_col":"blue", "fav_city":"winnipeg"}
jsonStr = json.dumps(data_toSave, indent=4) # converts python dictionary to json str 
fileOpen = open("files/new_sample.json","w") #open or create if non existent
fileOpen.write(jsonStr) 
print(fileOpen)

# using json.dumps() to combine the json obj & json file in one line  
jsonFile = open("files/new_sample_b.json", "w")
data_toSave_2= {"name":"mandy", "fav_col":"blue", "fav_city":["list",3,4,True,"abc"]}
json.dump(data_toSave_2, jsonFile, indent =4) # takes data_toSave_2 and adds it to the json file 

# Appending (a better way than just appending )
# 1. read in the entire contents of the file
# 2. append to the JSON object in python
# 3. write out the entire JSON object (overwrite the file)
jsonFile = open("files/new_sample_b.json", "r+") # read-write mode
data = json.load(jsonFile)
print(data['fav_city'])
print(type(data['fav_city']))
jsonFile.seek(0) # go to beginning of file
data['fav_city'].append("another element")
data["newKey"] = 1234 # output to the file
json.dump(data,jsonFile, indent =4)