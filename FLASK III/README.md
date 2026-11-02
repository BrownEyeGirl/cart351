CART 351 FALL 2026
Home
Course-Outline
Schedule
Exercises
Lectures
Mini-Projects
Readings
QuickLinks
FLASK III & FETCH
Last week we covered:
Jinja Templates & Inheritance
Passing variables into the Jinja HTML templates
Reviewing if statements and for loops in using Jinja
Using url_for()
Implementing an HTML form and sending a GET request with arguments to Flask, processing those arguments and passing the arguments into another HTML page...
This week we will cover:
More on Get Requests
Sessions
The Post Request
Using client side Javascript to send/receieve data from the web server
More on GET Requests
Recall last week:
- we had issues whereby once we sent data with the GET request:

we either could choose to have access to the data BUT the url would not be reset,
or we performed a REDIRECT and lost access to the data.
So the question is now how can we store the data if we want to have access to it later? ... and so we start with sessions:

Sessions in Flask
Since HTTP is a stateless protocol, each request has no knowledge of any requests previously executed ...

While this greatly simplifies client/server communication, web applications typically need a way to store data between each request as a user interacts with the application itself.

For example, on a shopping site: one needs to store items that a non authenticated user has added to their "cart" - and not necessarily in a database... so you can use sessions .

A session is used to store information related to a particular user, across different requests. The data stored for a session should be considered temporary data - because the session will eventually expire.
To permanently store data, you need to use a database. There are two types of commonly used sessions in web dev:

Client-side:sessions are stored client-side in browser cookies
Server-side:sessions are stored server-side (typically a session identifier is then created and stored client-side in browser cookies)
Flask uses the client-side approach: To store data across multiple requests, Flask utilizes cryptographically-signed cookies (stored on the web browser) to store the data for a session.
This cookie is sent with each request to the Flask app on the server-side where it's decoded...
Note: this is not a secure option - so these type of sessions should not be used to store sensitive information.

Let's build a couple of examples to show how sessions work and how we can use them to our benefit:

Adding session variables
We can start with this starter project from last week:
Start by creating a new HTML template ie inputSessionData.html :

<!-- will be a child of base-->
{% extends "base.html" %}
{% block content %}
<h3>SAVE SESSION VARS</h3>
<div class= "sessionVars">
<!-- take out the form action etc..-->
<form id="sessionStore" method = "GET" action="/saveSession">
    <p><label>DATA A:</label>
    <input type="text" size="24" maxlength="40" name="data_a" required>
  </p>  
  <p><label>DATA B:</label>
    <input type="text" size="24" maxlength="40" name="data_b" required>
  </p>  
 <p><label></label>
  <input type="submit" name="submit" value="send" id=buttonS /></p>
</form>
</div>
{% endblock %}

Also add to base.css:

.sessionVars{
    background:white;
    width:50%;
    padding:10px;
}
.sessionVars input[type=submit]{
    width:100px;
    margin-top:10px;
}

We will also add a route in main.py:

#add session route
@app.route('/inputSessionData')
def inputSessionData():
    return render_template("inputSessionData.html")

Ok - we are ready to handle sessions:)
First: we need to add a secret key in main.py (is a property of the app variable):

# Details on the Secret Key: https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.
app.secret_key = 'BAD_SECRET_KEY'


and ensure that you import 'session' (your import statement should look like):

from flask import Flask, render_template, request, session, redirect,url_for

Next: you can see in the HTML form that we want to send the data to /saveSession:
So lets set that up in main.py:

@app.route('/saveSession')
def saveSession():
    app.logger.info(request.args['data_a'])
    #reload  - use url_for() here :) - the function...
    #but note that the data will be gone
    # so add in a session variable
    session['data_a'] = request.args['data_a']
    session['data_b'] = request.args['data_b']
    return redirect(url_for('inputSessionData'))

So - Flask uses an inbuilt dictionary object called session to store the session variables...
and we can so easily just save to them :) - and then we redirect!

Now - we can add in some more content in our HTML template... why?
Because you will see that you can super easily access the session data within your Jinja template ;)
So add to inputSessionData.html (after the div tag):

{%if session['data_a']%}
<h3>LOAD SESSION VARS</h3>
<p> Data A: {{session['data_a']}}</p>
<p> Data B: {{session['data_b']}}</p>
{% endif %}

Super! So the view has changed because the session vars are active :) And if you go in your browser to the Application Tab > Storage > Cookies.. you should see an entry :)
Details to view and decode in the browser:
Press F12 (or Cmd + Option + I on Mac) to open Chrome DevTools.
Click on the Application tab at the top of the DevTools panel
From the Storage heading in the left side bar expand the Cookies dropdown and select your Flask app's URL (e.g., http://127.0.0.1:5000).
Look for the cookie named session. The long string of text in the Value column is your signed session data
Flask cookie values look like this: eyJ1c2VyX2lkIjoxfQ.ZxeHIw... (three sections separated by periods).
The very first section contains your session variables encoded in Base64. You can decode it using a quick method:
Double-click the Value cell of the session cookie in DevTools and copy the text.
Switch to the Console tab in DevTools.
Paste the first segment of the cookie (everything before the first period .) into the following code and run it
(atob() is a built-in JavaScript function that decodes a string of Base64-encoded data back into its original form.):
    atob("YOUR SEGMENT HERE")
    
Modifying session variables
Let's add on here and say you want to modify the session variables ;)

Start by making a new html page - i.e. modifySessionData.html:

<!-- will be a child of base-->
{% extends "base.html" %}
{% block content %}

{%if session['data_a']%}
<h3>A NEW PAGE WITH THE SESSION VARS</h3>
<p> Data A: {{session['data_a']}}</p>
<p> Data B: {{session['data_b']}}</p>

<h4 style = "margin-top:20px"> Modify session vars:</h4>
<form method = "get" action = "/modifySession">
<div class= "sessionVars">
<p><label>DATA A:</label>
<input type="text" size="24" maxlength="40" name="data_a" value = {{session['data_a']}} required>
</p>  
<p><label>DATA B:</label>
    <input type="text" size="24" maxlength="40" name="data_b" value = {{session['data_b']}} required>
  </p>   
  <p><label></label>
<input type = "submit" value = "submit"/>
  </p>
</form>
</div>

{% else %}
<h3>NO SESSION VARS </h3>
<a href = "{{url_for('inputSessionData')}}">back to input session vars</a>
{% endif %}
{% endblock %}

And add a route to main.py:

#modify session route
@app.route('/modifySessionData')
def modifySessionData():
    return render_template("modifySessionData.html")

So - you should see already when we load this page that you have access to the session data...
we can then make a route in main.py to process the modifications:

@app.route('/modifySession')
def modifySession():
    app.logger.info(request.args['data_a'])

    #reload  - use url_for here :) - the function...
    #but note that the data will be gone
    # so add in a session variable
    session['data_a'] = request.args['data_a']
    session['data_b'] = request.args['data_b']
    return redirect(url_for('modifySessionData'))

And now when you rerun - and submit the form ... the session variables change!
We can easily verify that this change carries over to the inputSessionData.html.
Add in the current html (modifySessionData.html) another link (after the form)

<a href = "{{url_for('inputSessionData')}}">back to input session vars</a>

Delete Session Data
Lastly, lets in the modifySessionData.html add in the option to delete the session data...
Add the following to the page:

<div class= "sessionVars" style = "background: rgb(232, 178, 233);">
<h4> CLICK the button to DELETE session vars:</h4>
<form method = "get" action = "/deleteSession">
<input type = "submit" value = "submit"/>
</form>
</div>

And then of course a route in main.py to process the form:
 
@app.route('/deleteSession')
def deleteSession():
    # Clear the session data stored in the session object
    session.pop('data_a', default=None)
    session.pop('data_b', default=None)
    return redirect(url_for('modifySessionData'))

You can also add another link in the FIRST if block in the inputSessionData.html
 
<a href = "{{url_for('modifySessionData')}}">go to modify page</a>

And test :) :)
Small Exercise::: lets add a counter that will increment every time we modify the session data ... - and store it as its own session variable

Submit A Form Without Reloading the Page using the Fetch API using GET
In this section, we are going to submit a form once again using GET an but we will use now use JavaScript and the Fetch API in order to circumvent the need for page reloading / redirection.
We will submit the SAME form that we did last week (with plants) - but reworked ;) Let us continue with the same project as before:

We will add another block to base.html, to dynamically add js to a page:
 
    <!--new add a custom block for the script-->
    {% block scriptblock %}
    {% endblock %}

So, with the base template (base.html) already in place, we will generate a new page for inserting the data:
form_fetch.html, making them it inherit from base.html.
 
<!-- will be a child of base-->
{% extends "base.html" %}
<!-- js for this page-->
{% block scriptblock %}
  <script src="{{url_for('static',filename='js/script_get.js')}}"></script>
{% endblock %}

{% block content %}
<h3> PROCESS FORM WITH GET AND FETCH</h3>
    <section class = "plant-collect">
    <div class= "formContainer">
<form id = "insertPlantFormFetch">
<!-- group the related elements in a form -->
<h3> ADD A NEW PLANT</h3>
<fieldset>
 <p>
    <label>Owner Name:</label>
    <input type="text" size="24" maxlength = "40" name = "o_name" required> 
</p>
<p>
    <label>Plant Name:</label>
    <input type="text" size="24" maxlength = "40" name = "p_name" required> 
</p>
<p>
    <label>Plant Color:</label>
    <input type="color" name = "p_color" required> 
</p>
<div class="range-ui">
<label>Plant Condition:</label>
<div>
  <input type="range" name="p_condition" min="0" max="100" value="0" step="1" list="values" />
  <datalist id="values">
  <option value="0" label="almost dead!"></option>
  <option value="100" label="super-alive"></option>
</datalist>
</div>
</div>
<p>
  <label>Home of Plant:</label>
  <select name="plant-home" >
  <option value="Montreal">Montreal</option>
  <option value="Quebec City">Quebec City</option>
  <option value="Ottawa">Ottawa</option>
  <option value="Winnipeg">Winnipeg</option>
  <option value="Vancouver">Vancouver</option>
</select>
</p>
<p>
    <label>Birth Date (DD-MM-YYYY):</label>
    <input type="date" name="a_date" required>
</p>
<p>
    <label>Description:</label>
    <textarea type = "text" rows="4" cols="50" name = "a_descript" required></textarea>
</p>
 <p>
    <label></label>
    <input id = "submitPlant" type = "submit" name = "submit" value = "submit my info" id =buttonS />
</p>
 </fieldset>
</form>
</div>
<div id="results">
  <h4>RESULTS</h4>
  <div id="result-container">
    </div>
</div>
</section>
{% endblock %}

OK - so this is very similar to the previous form examples EXCEPT:
We left the action attribute of the form empty
We took out the method attribute of the form
We added an id called "insertPlantFormFetch" to the form
We added a div with id called "result" in order to hold the results....
Let's add some css for the result container to base.css:

/*** results **/
#results{
  margin-top:4vh;
  margin-bottom:4vh;
  color:rgb(211, 172, 209);
  font-size:18px;
}
#result-container{
    padding:1%;
    background: rgb(211, 172, 209);
    width:50%;
    font-size:14px;
    color:white;
  
}
#result-container p{
  padding:4px;
   font-size:16px;
}
#result-container p mark{
  color: rgb(211, 172, 209);
  background:white;
  padding:2px;
}
#result-container img{
  width:80%;
  height: auto;

}

ACCESS THE FORM WITH JS
Instead of automatically sending the form as was done earlier, we will instead use the fetch function to access the form data.
If you see - in the form_fetch_get.html page, we included a link to a javascript file -- you will need to create it: js/script_get.js

We first need to detect when the form is to be submitted -> add the following into the script :
 
window.onload = function () {
  console.log("loaded script_get.js");
  document
    .querySelector("#insertPlantFormFetch")
    .addEventListener("submit", async function (event) {
      event.preventDefault();
      console.log("button clicked");
    });
};

Now - add the route to this new page in main.py:
 
# aroute
@app.route('/getForm')
def getFetchForm():
    return render_template("form_fetch.html")

If you now run the page -> and click on the submit button, the line button clicked should be output to the console.
If you have not input data into all the required fields, then the initial validation still occurs:: why?
We are still using the submit event - > which triggers the basic form validation.. -
GETTING THE DATA FROM THE FORM
Now we want to access the form data - there are multiple ways of doing this:
Get the value of each field -> this is really long winded and since we want all the fields in the form we will find another option:
We will get the form element by its id:
 
 const htmlForm = document.querySelector("#insertPlantFormFetch");
 
We will use the inbuilt JavaScript FormData object:
 
 const formData = new FormData(htmlForm);
 
This object: FormData can take an HTML form as a parameter upon making a new instance, and will automatically populate the object with the form's current keys & values using the name property of each element for the keys and their submitted value for the values.

We will next need to format our key value pairs as query parameters - we could do this manually, but thee is a super javascript object that will do it for us: URLSearchParams:
 
const queryParams = new URLSearchParams(formData).toString();

Ok - now we can build the URL :remember we are doing a GET request...:

const url = `/getDataFromForm?${queryParams}`;

Finally: the next step is to use a javascript method to send the data to our flask application:

 try{
     let res = await fetch(url)
     let resJSON = await res.json()
       console.log(resJSON)

  }
    catch(err) { 
    console.log(err)
  }
  
SIDE TOPIC: THE JS FETCH REQUEST:

You start a Fetch Request with the fetch function and pass it a URL (the location for where the data resides) as an argument.
By default one will make a request for the resource, and the function will respond with a promise.
A Promise (which is a newish -> now almost standard convention in JS) on a high level represents the eventual fulfillment/failure of an asynchronous event (i.e. a request for a remote resource).
In the case of the fetch() - the resulting promise will automatically resolve to the Response object representing the server's response
You can then check the request status and extract the body of the response in various formats, including text and JSON, by calling the appropriate method on the response-> text() or json()
It is good practise to execute the fetch request within a try/catch clause
You will need to use the await keyword BOTH for fetching and parsing because these are operations that may take some time...
AND we need to wrap the whole thing in an async function...
BACK IN OUR FLASK APP
We will now write the python code to deal with this request.... very similar to what we did previously... The first step is to set up a new route in main.py:

# for the get
@app.route('/getDataFromForm')
def getDataFromForm():
    app.logger.info(request.args)
    return ({"data_received":"success",
    "owner":request.args['o_name'],
    "plantname":request.args['p_name']})

Note:: the change is: we are no longer going to reload/redirect to a new page - rather we will send whatever response back to the caller (in this case the script.js) and then use javascript to dynamically generate markup :)

Back in the script_get.js -you see where we get a response back from the server?... Well that is where we will generate a the JS markup.

document.querySelector("#result-container").innerHTML += 
       ` THE NEW RESULT: ${resJSON.data_received}
        OWNER NAME : ${resJSON.owner}
        PLANT NAME : ${resJSON.plantname}`
  
  
And we are done! ... It seems to be alot of work - but you will see in the next example that doing a POST request is very much the same...

Uploading an image :) with FETCH
Ok! So as the last topic in this session, we will look at sending multi part form data. It is a strategy/method for sending multiple types of data in a single HTTP request, commonly used for file uploads and submitting forms with various input types.

We will once again be continuing with the same project as before. We will use the same HTML form as the one we used to add-to-the-plant-repository, but we will extend and adapt the functionality to include the ability to upload a file to the web server. We wil be using this time POST and FETCH.

Create a new html template and save as addPlantExtended.html. Add the following markup:

  <!-- will be a child of base-->
{% extends "base.html" %}

{% block scriptblock %}
  <script src="{{url_for('static',filename='js/script_post.js')}}"></script>
{% endblock %}
{% block content %}
    <section class = "plant-collect">
    <div class= "formContainer">
<!--form done using more current tags... -->
<form id = "insertPlantFormFetchPost">
<!-- group the related elements in a form -->
<h3> ADD A NEW PLANT AND AN IMAGE </h3>
<fieldset>
 <p>
    <label>Owner Name:</label>
    <input type="text" size="24" maxlength = "40" name = "o_name" required> 
</p>

<p>
    <label>Plant Name:</label>
    <input type="text" size="24" maxlength = "40" name = "p_name" required> 
</p>

<p>
    <label>Plant Color:</label>
    <input type="color" name = "p_color" required> 
</p>
<div class="range-ui">

<label>Plant Condition:</label>

<div>
  <input type="range" name="p_condition" min="0" max="100" value="0" step="1" list="values" />
  <datalist id="values">
  <option value="0" label="almost dead!"></option>
  <option value="100" label="super-alive"></option>
</datalist>
</div>

</div>

<p>
  <label>Home of Plant:</label>
  <select name="plant-home" >
  <option value="Montreal">Montreal</option>
  <option value="Quebec City">Quebec City</option>
  <option value="Ottawa">Ottawa</option>
  <option value="Winnipeg">Winnipeg</option>
    <option value="Vancouver">Vancouver</option>
</select>
</p>
<p>
    <label>Birth Date (DD-MM-YYYY):</label>
    <input type="date" name="a_date" required>
</p>
<p>
    <label>Description:</label>
    <textarea type = "text" rows="4" cols="50" name = "a_descript" required></textarea>
</p>
<p>
    <label>Upload Image:</label>
    <input type="file" name='the_file' size=10 required />
</p>
 <p>
    <label></label>
    <input id = "submitPlant" type = "submit" name = "submit" value = "submit my info" id =buttonS />
</p>
 </fieldset>
</form>
</div>
<div id="results">
  <h4>RESULTS</h4>
  <div id="result-container">
    </div>
</div>
</section>
{% endblock %}
  
  
You will also need to set up a route to this page in main.py:

# another route
@app.route('/addPlantExtended')
def addPlantExtended():
    return render_template("addPlantExtended.html")

We will use a new js file linked to this page ( script_post.js ). So create this file, save in the js folder, and then we will process the form using js! So first we need to know when we have submitted the form - when the window has loaded the content:

window.onload = function () {
  console.log("loaded script_post.js");
 document
    .querySelector("#insertPlantFormFetchPost")
    .addEventListener("submit", async function (event) {
      event.preventDefault();
      console.log("post form clicked")
})
};

Next: as before - we will format the data from the form and package it using the formData object:

    let form = document.querySelector("#insertPlantFormFetchPost");
    let data = new FormData(form);

And then: once again we will use the fetch() - but this time we specify that the method to use is POST and also the data is assigned to the body property within the request ...

try {
        let res = await fetch("/postPlantFormFetch", {
          method: "POST",
          body: data,
        });
        let resJSON = await res.json();
        console.log(resJSON);
      } catch (err) {
        console.log(err);
    }

BACK IN THE FLASK APP
We will need to add some configuration to our flask app:
import os package (as we will be accessing the file system)
we will need to specify what folder files will be uploaded to
we will set a size limit for the max file size to be uploaded.
So - fist make a folder in the folder named 'static' of your project and call it uploads. Then add the following import statement:

import os

Next, add the following to main.py:

UPLOAD_FOLDER = 'static/uploads' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit

Next: we need to set up a route for where the data should be received to: "/postPlantFormFetch" and that this route must accept a request via the POST method:

@app.route("/postPlantFormFetch",methods = ['POST'])

And we add the function associated ...
 
def postPlantFormFetch():
     #key is the same as in the form :)
    uploadedfile = request.files['the_file']
    #save file to uploads folder
    filePath = os.path.join(app.config['UPLOAD_FOLDER'], uploadedfile.filename)
    app.logger.info(filePath)
    uploadedfile.save(filePath)
    app.logger.info(uploadedfile.filename)
     # the textual data will be in request.form 
    app.logger.info(request.form)
    #return the file name + path
    return({"imagePath":filePath})
  
Again we are NOT redirecting/reloading the page ... no we are passing back the filepath of the saved image ... And what we will do is - in the js we will dynamically display the new image - cause we have its file path ... So - in the js add:
 
 document.querySelector("#result-container").innerHTML = `<img src = ${resJSON.imagePath} />`
 
