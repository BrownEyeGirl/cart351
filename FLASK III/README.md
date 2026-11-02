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