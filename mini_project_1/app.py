import os, shutil, psutil
from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    #ram_free = round(psutil.virtual_memory().available / 1e9, 1) # convert bytes to gigabytes then round to nearest 10th decimal 
    #ram_total = round(psutil.virtual_memory().total / 1e9, 1)
    #disk_free = round(shutil.disk_usage(os.path.expanduser("~")).free / 1e9, 1)

    return render_template("index.html", info=read()) #ram_free=ram_free, ram_total=ram_total, disk_free=disk_free)


# read saved info, fall back to zeros if file is missing or wrong
DATA_FILE = "userinfo.json"

def read():
    info = {
        "clicks": 0, 
        "tab_leaves": 0,
        "ram_free_gb": round(psutil.virtual_memory().available / 1e9, 1),
        "ram_total_gb": round(psutil.virtual_memory().total / 1e9,  1),
        "disk_free_gb": round(shutil.disk_usage(os.path.expanduser("~")).free / 1e9,  1),
        "disk_total_gb": round(shutil.disk_usage(os.path.expanduser("~")).total / 1e9, 1),
    }

    try:
        with open(DATA_FILE) as f:
            info.update(json.load(f))
    except (FileNotFoundError, ValueError, TypeError):
        pass
    return info

# add one to an event (clicks or tab_leaves), save, return totals
@app.route("/log", methods=["POST"])
def log():
    event = (request.get_json(silent=True) or {}).get("event")
    info = read()
    if event in ("clicks", "tab_leaves"):  # ignore anything else
        info[event] += 1
        with open(DATA_FILE, "w") as f: # open as write only 
            json.dump(info, f) # add info to file 
    return jsonify(info)


# add one click, save to json, return total
# @app.route("/click")
# def click():
#     try:
#         clicks = json.load(open("clicks.json"))["clicks"]
#     except (FileNotFoundError, ValueError):
#         clicks = 0
#     clicks += 1
#     json.dump({"clicks": clicks}, open("clicks.json", "w"))
#     return jsonify(clicks=clicks)



if __name__ == "__main__":
    app.run(debug=True)

