
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
    return({"inFile":"false"}) 


app.run(debug = True)