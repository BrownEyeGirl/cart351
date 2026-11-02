
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__) # flask web application
app.secret_key = 'BAD_SECRET_KEY' # Details on the Secret Key: https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing the session data.

#DEFAULT ROUTE
@app.route('/')
def index():
   return render_template("index.html",
                           user={"username":"sabine"},
                           passedDictionary={
                                            "fav_color":"fuscia", 
                                             "fav_veg":"cauliflower",
                                             "fav_fruit":"kiwi",
                                             "fav_animal":"toucan"
                                             },
                            imgPath = "../static/images/pineapple_2.jpg"
                                        
                        )

# INPUT FORM
@app.route("/inputPlant")
def addPlantData():
    return render_template("addPlantData.html") 

#@app.route("/thank_you")
#def thank_you():
    #app.logger.info(request.args)
    #return render_template("thankyou.html") 
    #return render_template("thankyou.html",owner_name = request.args["o_name"]) 
    #return render_template("thankyou.html",plantData = request.args) 

#THANKS
@app.route("/thank_you")
def thank_you():
    app.logger.info(request.args)
  
    if('o_name' in request.args):
        owner_name = request.args["o_name"] 
        app.logger.info("first run to redirect")
         #url is not clean
        #return render_template("thankyou.html",plantData = request.args) 
        
        # issue we lose the parameters! - but url is clean :)
        return redirect(url_for("thank_you")) 
    #part of the reloading process... we redirect - then headers rewritten and reload the template
    else:
        app.logger.info("reloaded and redirected")
        return render_template("thankyou.html") 
#error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#register
@app.route("/register")
def register():
     return render_template("register.html")

@app.route("/reg_thank_you",methods = ['POST', 'GET'])
def reg_thank_you():
     app.logger.info(request.method)
     app.logger.info(request.form)
     app.logger.info(request.form["f_name"])
     app.logger.info(request.form["l_name"])
     fName = request.form["f_name"]
     lName = request.form["l_name"]
     return render_template("thankyou_reg.html", fName = fName, lName=lName)
     #return render_template("thankyou_reg.html")


#add session route
@app.route('/inputSessionData')
def inputSessionData():
    return render_template("inputSessionData.html")

# save session route 
@app.route('/saveSession')
def saveSession():
    app.logger.info(request.args['data_a'])
    #reload  - use url_for() here :) - the function...
    #but note that the data will be gone
    # so add in a session variable
    session['data_a'] = request.args['data_a']
    session['data_b'] = request.args['data_b']
    return redirect(url_for('inputSessionData'))



app.run(debug=True)