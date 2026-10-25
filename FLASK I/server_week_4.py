from flask import Flask,render_template

app = Flask(__name__) # create flask app


@app.route('/')
def index():
    return render_template("pineapple_two.html") # render template as the html file 

@app.route('/another')
def another():
    return render_template("pineapple_two.html")

@app.route('/three') # add another new route in the python file:
def three():
    someNewVar = "Sabine" # passing variable to a template 
    return render_template("pineapple_three.html",my_variable = someNewVar) # creates a variable to use in the html file 




app.run(debug=True)

