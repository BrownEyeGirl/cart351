

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
print(allLines[0]) # prints the first line 

# Open sample_text.txt with write+ mode
st = open("files/sample_text.txt", "w+")