from flask import Flask # flask is the package, Flask is the class in the package 

app = Flask(__name__)

@app.route("/")

def index(): 
    return ' Hello CART 351'

@app.route("/about")

def about():
    return '<h1 style = "color:purple"> About Cart 351!</h1>'


@app.route("/user/<name>")
def user_profile(name):
    # we will use templates sooN!
    return f"<h2> This is <span style = 'color:orange'>{name}'s</span> profile page" 

@app.route("/another/<dynamicVar>")
def another_route(dynamicVar):
    # we will use templates sooN!
    return f"<h2> the 100th letter of {dynamicVar} is {dynamicVar[-1]}</h2>"

@app.route("/catlatin/<word>")
def cat_latin(word):
    if(word[-1].lower() != "y"):
        return f"{word}y"
    return f"{word[:-1]}iful"

app.run(debug = True) # type python main.py in terminal to run. (debug = True) will guve you an error instead of just not working. 