#!/usr/bin/python3
import os
from flask import Flask, redirect, session, url_for, render_template, request, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy

CLIENT_ID = "omNihUKDY7L8XXLh41WTTY9Pda21T2SRqAmJO86C"
CLIENT_SECRET = "fmdfCpUwDIu0E5FExHudOdySDSa7HPhNrRKTirNsXJIWc2NEMFJtiY7UaczcTJL2kzRnsBV4OWPQ8P8KTv8YDqS5rdOOAE0opdYBLbZtMzNTfnCWHTJTgmpmDDtSbjDY"
REDIRECT_URI = "https://dev.wzhang.me/login"

AUTH_BASE_URL = "https://ion.tjhsst.edu/oauth/authorize/"
TOKEN_URL = "https://ion.tjhsst.edu/oauth/token/"

from requests_oauthlib import OAuth2Session
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models

# print(os.environ['APP_SETTINGS'])


oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=["read"])

authorization_url, state = oauth.authorization_url(
    AUTH_BASE_URL)


@app.route("/")
def index():
    if "oauth_token" in session:
        return render_template("main.html")
    session["oauth_state"] = state
    return redirect(authorization_url)


@app.route("/login", methods=["GET"])
def login():
    token = oauth.fetch_token(
        TOKEN_URL,
        code=request.args.get("code"),
        client_secret=CLIENT_SECRET)
    try:
        profile = oauth.get("https://ion.tjhsst.edu/api/profile")
    except TokenExpiredError as e:
        args = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
        token = oauth.refresh_token(
            "https://ion.tjhsst.edu/oauth/token/", **args)
    session["oauth_token"] = token
    return redirect(url_for('index'))


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
