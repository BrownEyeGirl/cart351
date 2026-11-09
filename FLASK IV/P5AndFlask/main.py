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
        app.logger.info("file exists")
        jsonFile = open(filePath, "r+")
        theList = json.load(jsonFile)
    else:
        app.logger.info("file not exists")
        #open file for writing
        jsonFile = open(filePath, "w")
        list_m = [request.args]
        json.dump(list_m, jsonFile, indent =4)
        jsonFile.close()


    return({"inFile":"false"})


app.run(debug = True)