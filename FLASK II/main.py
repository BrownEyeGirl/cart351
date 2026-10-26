from flask import Flask,render_template,request,redirect # request is used to get data from a form, render_template is used to render the html templates


app = Flask(__name__)

# super simple routing function to pass data to index.html
# @app.route('/')
# def index():
#     return render_template("index.html")

# new complex routing function to pass data to index.html
@app.route("/")
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


# new routing function to pass data to child templates of pineappleParent.html
@app.route("/pineappleA")
def pineAppleA():

    return render_template("pineappleChild.html",
                           dataPassedA = "child A!" )

@app.route("/pineappleB")
def pineAppleB():
    return render_template("pineAppleChild_B.html",
                           passedImg = "pineapple_2.jpg" ) # simplified but same as "../static/images/pineapple_2.jpg" ), can access data in static files


# for the add plant data form, create a new route for the form page 
@app.route("/inputPlant")
def addPlantData():
    return render_template("addPlantData.html") 


@app.route("/thank_you") # when the user clicks the submit button in addPlantData.html, a GET request will be automatically made for the " /thank_you" route
def thank_you():
    # app.logger.info(request.args) # the DATA that is in the HTML form will be automatically included in the request object, the the key args is a dictionary of key/value pairs, that are in actually the names and values of the form fields
    # return render_template("thankyou.html") # simply render the thankyou.html page, but we want to pass the data from the form to the thankyou.html page
    # return render_template("thankyou.html", owner_name = request.args.get("ownerName")) # option1: passes the owner_name to the thankyou.html page, the value of the ownerName field in the form is accessed using request.args.get("ownerName"), which is a method that returns the value of the specified key in the dictionary, if it exists, otherwise it returns None
    # return render_template("thankyou.html", plantData = request.args)  # option2: passes the entire request.args dictionary to the thankyou.html page, which can be accessed using {{ plantData['o_name'] }} or other values in the template

    app.logger.info(request.args)
  
    if('o_name' in request.args):
        owner_name = request.args["o_name"] 
        app.logger.info("first run to redirect")
         #url is not clean
        return render_template("thankyou.html",plantData = request.args) 
        
        # issue we lose the parameters! - but url is clean :)
        return redirect(url_for("thank_you")) 
    #part of the reloading process... we redirect - then headers rewritten and reload the template
    else:
        app.logger.info("reloaded and redirected")
        return render_template("thankyou.html") 

# error handler 

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

app.run(debug=True)
