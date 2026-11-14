import os, shutil, psutil
from flask import Flask, render_template, jsonify, request, session
from datetime import datetime

app = Flask(__name__)

# needed to sign the session cookie ( uses a placeholder like this for testing)
app.secret_key = 'BAD_SECRET_KEY'

# build the info dictionary: this visitor's session values + live system stats
def read():
    info = {
        "clicks": session.get("clicks", 0),
        "tab_leaves": session.get("tab_leaves", 0),
        "first_visit": session.get("first_visit"),
    }

    # live stats are not saved, they are measured fresh each time
    info.update({
        "ram_free_gb": round(psutil.virtual_memory().available / 1e9, 1), # turns into gb and rounds to nearest 10th 
        "ram_total_gb": round(psutil.virtual_memory().total / 1e9, 1), # ''
        "disk_free_gb": round(shutil.disk_usage(os.path.expanduser("~")).free / 1e9, 1),
        "disk_total_gb": round(shutil.disk_usage(os.path.expanduser("~")).total / 1e9, 1),
    })
    return info

@app.route("/")
def index():
    # first visit from THIS browser, only saved once
    if "first_visit" not in session:
        session["first_visit"] = datetime.now().isoformat(timespec="seconds")
    return render_template("index.html", info=read())

# add one to an event (clicks or tab_leaves), store in the session, return totals
@app.route("/log", methods=["POST"])
def log():
    event = (request.get_json(silent=True) or {}).get("event")
    if event in ("clicks", "tab_leaves"):  # ignore anything else
        session[event] = session.get(event, 0) + 1
    return jsonify(read())

# read-only route for the buttons (does not count as a click)
@app.route("/info")
def info_route():
    return jsonify(read())

print(app.secret_key)
if __name__ == "__main__":
    app.run(debug=True, port=5000) # change port if page is not loading. sometimes it glitches. 