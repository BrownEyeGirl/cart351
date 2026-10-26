from flask import Flask,render_template
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

    return render_template("pineappleChild_B.html",
                           passedImg = "../static/images/pineapple_2.jpg" )



app.run(debug=True)