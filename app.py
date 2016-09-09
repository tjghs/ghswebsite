import os
from flask import Flask, render_template, request, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models

print(os.environ['APP_SETTINGS'])


@app.route("/")
def index():
    return render_template("main.html")    

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('static/css', path)

@app.route("/scripts/<path:path>")
def send_js(path):
    return send_from_directory('static/scripts', path)

@app.route("/icons/<path:path>")
def send_icons(path):
    return send_from_directory('static/icons', path)

@app.route("/fonts/<path:path>")
def send_fonts(path):
    return send_from_directory('static/fonts', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
