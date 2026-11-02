# FLASK III In-Class Lesson 
Link to lesson: https://anomalse.github.io/CART351-Fall-2026/lectures/flask_three.html 

## My Notes
<b>Activate virtual environemnts in VS Code terminal <br>
Create virtual environment<br>
conda create --name flaskEnv python=3.13 
pip install flask

Activate Virtual environment (if virtual environment already created)<br>
conda activate flaskEnv

To permanently store data, you need to use a database. There are two types of commonly used sessions in web dev:
Client-side:sessions are stored client-side in browser cookies
Server-side:sessions are stored server-side (typically a session identifier is then created and stored client-side in browser cookies)
Note: Flask uses Client-side. This is NOT a secure option, do not pass secret data. 

<i>Get vs Post requests</i>

request.form to get the data

View Session Data: 
If you go in your browser to the Application Tab > Storage > Cookies.. you should see an entry :)
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