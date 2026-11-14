import os, shutil, psutil
from flask import Flask, render_template, jsonify, request, make_response
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "userinfo.json"

# read saved info, then put live system stats on top
def read():
    info = {"clicks": 0, "tab_leaves": 0}

    try:
        with open(DATA_FILE) as f:
            info.update(json.load(f))
    except (FileNotFoundError, ValueError, TypeError):
        pass

    # live stats always win over saved ones
    info.update({
        "ram_free_gb": round(psutil.virtual_memory().available / 1e9, 1),
        "ram_total_gb": round(psutil.virtual_memory().total / 1e9, 1),
        "disk_free_gb": round(shutil.disk_usage(os.path.expanduser("~")).free / 1e9, 1),
        "disk_total_gb": round(shutil.disk_usage(os.path.expanduser("~")).total / 1e9, 1),
    })
    return info

# write info to json file
def save(info):
    with open(DATA_FILE, "w") as f:
        json.dump(info, f)

@app.route("/")
def index():
    info = read()
    now = datetime.now().isoformat(timespec="seconds")
    cookie = request.cookies.get("tv_first")

    # first visit to the whole site, only saved once
    if "first_visit" not in info:
        info["first_visit"] = now

    # new browser: add to the list of visitors
    if not cookie:
        info.setdefault("visits", []).append(now)
    save(info)

    resp = make_response(render_template("index.html", info=info, my_first=cookie or now))
    if not cookie:
        resp.set_cookie("tv_first", now, max_age=60 * 60 * 24 * 365)  # remember this browser for a year
    return resp

# add one to an event (clicks or tab_leaves), save, return totals
@app.route("/log", methods=["POST"])
def log():
    event = (request.get_json(silent=True) or {}).get("event")
    info = read()
    if event in ("clicks", "tab_leaves"):  # ignore anything else
        info[event] += 1
        save(info)
    return jsonify(info)

# simply reads the data and returns it 
@app.route("/info")
def info_route():
    return jsonify(read())

if __name__ == "__main__":
    app.run(debug=True, port=5001)