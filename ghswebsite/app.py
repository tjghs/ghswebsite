#!/usr/bin/python3
import sys
import os
from flask import Flask, redirect, session, url_for, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from ghswebsite.models import *
from ghswebsite.forms import *
from ghswebsite.views import *