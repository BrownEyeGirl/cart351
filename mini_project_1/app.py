import os, shutil, psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    ram_free = round(psutil.virtual_memory().available / 1e9, 1)
    ram_total = round(psutil.virtual_memory().total / 1e9, 1)
    disk_free = round(shutil.disk_usage(os.path.expanduser("~")).free / 1e9, 1)
    print("ram free: ", ram_free)
    return render_template("index.html", ram_free=ram_free, ram_total=ram_total, disk_free=disk_free)

if __name__ == "__main__":
    app.run(debug=True)

