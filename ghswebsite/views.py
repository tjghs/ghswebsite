#!/usr/bin/python3
import json
from flask import Flask, redirect, session, url_for, render_template, request, send_from_directory
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError
from urllib.parse import urlparse, urljoin

from ghswebsite.app import app, db
from ghswebsite.models import Hour, Announcement, User

AUTH_BASE_URL = "https://ion.tjhsst.edu/oauth/authorize/"
TOKEN_URL = "https://ion.tjhsst.edu/oauth/token/"


CLIENT_ID = app.config["CLIENT_ID"]
CLIENT_SECRET = app.config["CLIENT_SECRET"]
REDIRECT_URI = app.config["REDIRECT_URI"]
AUTH_BASE_URL = app.config["AUTH_BASE_URL"]
TOKEN_URL = app.config["TOKEN_URL"]


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and \
        ref_url.netloc == test_url.netloc


def get_redirect_target():
    for target in request.values.get("next"), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


def redirect_back(endpoint, **values):
    target = request.form["next"]
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)


@app.route("/")
def index():
    announcements = Announcement.query.all()
    return render_template("index.html", announcements=announcements)


@app.route("/hours/")
def hours():
    if "oauth_token" in session:
        profile_json = session.get("profile")

        hours = Hour.query.filter_by(user=profile_json['ion_username'])
        return render_template("hours.html", hours=hours)

    return redirect(url_for("login", next="hours"))


@app.route("/admin/", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        if "oauth_token" in session:
            # profile_json = session.get("profile", {})
            username = session.get("username", {})
            admins = ["2018wzhang", "2018nzhou"]
            if username in admins:
                announcements = Announcement.query.all()
                hours = Hour.query.all()
                return render_template(
                    "admin.html",
                    announcements=announcements,
                    hours=hours)
            return "Unauthorized"

        return redirect(url_for("login", next="admin"))
    elif request.method == "POST":
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("admin"))


@app.route("/login/", methods=["GET"])
def login():
    nexturl = request.args.get("next")
    if not is_safe_url(nexturl):
        return Flask.abort(400)

    oauth = OAuth2Session(
        CLIENT_ID, redirect_uri=REDIRECT_URI, scope=["read"])
    if "code" not in request.args:
        authorization_url, state = oauth.authorization_url(AUTH_BASE_URL)
        session["next"] = nexturl
        return redirect(authorization_url)
    try:
        token = oauth.fetch_token(
            TOKEN_URL, code=request.args.get(
                "code", ""), client_secret=CLIENT_SECRET)
        profile = oauth.get("https://ion.tjhsst.edu/api/profile")
        profile_data = json.loads(profile.content.decode())
        session["profile"] = profile_data
        session["username"] = profile_data["ion_username"]
        users = User.query.filter_by(username=session["username"])
        if users.count() == 0:
            newUser = User(
                profile_data["first_name"],
                profile_data["last_name"],
                profile_data["ion_username"],
                0)
            db.session.add(newUser)
            db.session.commit()
            print("New user " + session["username"] + " created.")

        session["oauth_token"] = token
        return redirect(url_for(session["next"]))
    except InvalidGrantError:
        return redirect(url_for("login"))


@app.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("static/css", path)


@app.route("/scripts/<path:path>")
def send_js(path):
    return send_from_directory("static/scripts", path)


@app.route("/icons/<path:path>")
def send_icons(path):
    return send_from_directory("static/icons", path)


@app.route("/images/<path:path>")
def send_images(path):
    return send_from_directory("static/images", path)


@app.route("/fonts/<path:path>")
def send_fonts(path):
    return send_from_directory("static/fonts", path)
