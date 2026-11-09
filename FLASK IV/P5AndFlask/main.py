import os
import json

from flask import Flask,render_template,request
app = Flask(__name__) # basic flask app 
# a route
@app.route('/') # default route (index.html)
def index():
    return render_template("index.html")


# another route
@app.route('/p5BreakOut')
def runpP5():
    return render_template("p5_BreakOut.html")


# for the get from p5
@app.route('/getDataFromP5')
def getDataFromP5():
    #give back request.args
    app.logger.info(request.args["id"])
    app.logger.info(request.args["score"])
    
      # Check if the file exists (can be a file or directory)
    filePath="filesForP5/p5Data.json"
    if os.path.exists(filePath):
        jsonFile = open(filePath, "r+")
        theList = json.load(jsonFile)
        nameExists = False
        oldData = ""
        for el in theList:
            if el["id"].upper() ==  request.args["id"].upper():
                nameExists = True
                oldData = el["score"]
                el["score"] = request.args["score"]
                break # This exits the loop entirely
        #clear 
        jsonFile.truncate(0)
        jsonFile.close()
        jsonFile_write = open(filePath, "w")
        if nameExists ==True: 
            json.dump(theList,  jsonFile_write, indent =4)
            jsonFile_write.close()
            return({"inFile":"true","score":oldData})
        else:
            theList.append(request.args)
            json.dump(theList, jsonFile_write, indent =4)
            jsonFile_write.close()
            return({"inFile":"false"})


    return({"inFile":"false"})


app.run(debug = True)