from django.shortcuts import render

# Create your views here.
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
ROOT_URL = app.config["ROOT_URL"]


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
    return render_template(
        "index.html",
        prefix=ROOT_URL,
        announcements=announcements)

@app.route("/hours/")
def hours():
    if "oauth_token" in session:
        profile_json = session.get("profile")
        users = User.query.filter_by(username=profile_json['ion_username'])
        hours = []
        if users.count() == 0:
            newUser = User(
                profile_json['first_name'],
                profile_json['last_name'],
                profile_json['ion_username'],
                [])
            db.session.add(newUser)
            db.session.commit()
            print("New user " + profile_json['ion_username'] + " created.")
        else:
            hours = Hour.query.filter_by(user=users[0].id)
        return render_template("hours.html", prefix=ROOT_URL, hours=hours)

    return redirect(url_for("login", next="hours"))


@app.route("/slideshow/<path:path>")
def slideshow(path):
    return send_from_directory("slideshow", path)


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
                users = []
                for hour in hours:
                    users.append(
                        User.query.filter_by(
                            id=hour.user)[0].username)
                return render_template(
                    "admin.html", prefix=ROOT_URL,
                    announcements=announcements, users=users,
                    hours=hours)
            return "Unauthorized"

        return redirect(url_for("login", next="admin"))
    elif request.method == "POST":
