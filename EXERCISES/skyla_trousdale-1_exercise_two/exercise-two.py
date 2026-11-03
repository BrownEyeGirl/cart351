from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)


# the default route
@app.route("/")
def index():
    return render_template("index.html")

#*************************************************
#Task-1: GET REQUEST
@app.route("/t1", methods=['GET']) # default is GET, but I specified it here for readability and my own understanding. 
def t1():
    return render_template("t1.html",have_results=False)
#*************************************************
@app.route("/getSearchCriteria")
def getSearchCriteria():
    app.logger.info(request.args)
    user_input = request.args['search_query'].replace(' ', '%20') # get users search query then replace the empty space to be url encoded
    nasa_API ="https://images-api.nasa.gov/search?q=" + user_input + "&media_type=image" # take api url and append the user input to it, then specify the media type to be image, so that we only get images back from the api
    
    data = requests.get(nasa_API).json() # make the request to the api using the url i just created, then get the response as json

    imgFromNasa = data['collection']['items'][0]['links'][0]['href'] # get the first image from the results, and get the href link to it
    description = data['collection']['items'][0]['data'][0]['description'] # get the description of the first image from the results
    
    return render_template("t1.html",
                                 have_results = True,
                                 description=description,
                                 imgPath = imgFromNasa           
                             )
    pass


#*************************************************
# #Task-2: GET REQUEST
@app.route("/t2")
def t2():
    return render_template("t2.html")
#*************************************************
@app.route("/getSearchCriteria_adv")
def getSearchCriteria_adv():
    app.logger.info(request.args)

    encoded_image_links = []

    user_input = request.args['search_query'] # get users search query 
    nasa_API ="https://images-api.nasa.gov/search?q=" + user_input + "&media_type=image" # take api url and append the user input to it, then specify the media type to be image, so that we only get images back from the api
    data = requests.get(nasa_API).json() # make the request to the api using the url i just created, then get the response as json

    for images in data['collection']['items']:
        singleImage = images['links'][0]['href']              # first image href
        encoded_image_links.append(singleImage.replace(' ', '%20'))  # url-encode spaces, add to list

    return render_template("t2.html",images=encoded_image_links)
    pass

#*************************************************

#run
app.run(debug=True)