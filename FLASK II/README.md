## Notes on Lesson Flask II 

# Setting up environment: 

# Notes: 
Jinja doesnt know what commenting out is, just delete html instead of commenting it out, otherwise it wont work.


# Request Object Data
In Flask, the Request Objectis an object that contains all the data sent from the Client to Server.
This data can be recovered using the GET/POST Methods.
Here is a partial list of some important properties and what they contain:
request.method: Returns the HTTP method used for the request (e.g., "GET", "POST", "PUT", "DELETE").
request.url: Provides the full URL of the requested page.
request.form: A dictionary-like object containing data submitted in the request's form, typically used for POST requests.
request.args: A dictionary-like object containing query parameters passed in the URL, commonly used for GET requests.
request.files: A dictionary-like object holding information about any files uploaded in the request.
request.cookies: A dictionary-like object containing any cookies sent with the request by the client.
request.data: Returns the raw, buffered request body, useful for handling non-form data like JSON or XML.
request.json: If the request body contains JSON, this attribute automatically parses it into a Python dictionary or list.
So - to complete this example - we will access the data that was passed with the post request in python.
In main.py, within the reg_thank_you() add:

app.logger.info(request.method)