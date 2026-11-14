import os, shutil, psutil
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    ram_free = round(psutil.virtual_memory().available / 1e9, 1) # convert bytes to gigabytes then round to nearest 10th decimal 
    ram_total = round(psutil.virtual_memory().total / 1e9, 1)
    disk_free = round(shutil.disk_usage(os.path.expanduser("~")).free / 1e9, 1)
    print("ram free: ", ram_free)
    return render_template("index.html", ram_free=ram_free, ram_total=ram_total, disk_free=disk_free)


# clicks function read saved clicks, fall back to 0 if file is missing or wrong
def read():
    try:
        with open("clicks.json") as c:
            return int(json.load(c)["clicks"])
    except (FileNotFoundError, ValueError, KeyError, TypeError):
        return 0
    

# add one click, save to json, return total
@app.route("/click")
def click():
    try:
        clicks = json.load(open("clicks.json"))["clicks"]
    except (FileNotFoundError, ValueError):
        clicks = 0
    clicks += 1
    json.dump({"clicks": clicks}, open("clicks.json", "w"))
    return jsonify(clicks=clicks)



if __name__ == "__main__":
    app.run(debug=True)

