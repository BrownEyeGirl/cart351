

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
    a_name = input("Enter the name of the animal: ") # get user input 
    sampleFile.write(a_name) # write input in file 
    sampleFile.write("\n") # enter to next line 
#sampleFile.close() # safer to close it, conserves resources. although lines written immediately even without closing
print("Data is written into the file.") 

# Ask for colours 
colorList = [] 
for i in range(3): 
    a_name = input("Enter the name of a color: ") 
    colorList.append(a_name + '\n') 
sampleFile.writelines(colorList) 
sampleFile.close() 
print("Data is written into the file.") 


""" APPENDING A TEXT FILE """

sampleFile_a = open("files/sample_text.txt", "a") # the ONLY difference is you open it for appending rather than writing. if opened with "w", it would rewrite what already exists. 
nameList = [] 
for i in range(3): # repeats 3x, [0,1,2]
    a_name = input("Enter the name of someone in your class: ") 
    nameList.append(a_name + '\n') 
sampleFile_a.writelines(nameList) 
sampleFile_a.close() 
print("Data is written into the file.") 
