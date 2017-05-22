#!/usr/bin/python3
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from ghswebsite.app import app


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''  # key here
    SQLALCHEMY_DATABASE_URI = ''  # Postgres url here


class ProductionConfig(Config):
    CLIENT_ID = ""  # OAuth client ID here
    CLIENT_SECRET = ""  # OAuth client secret here
    REDIRECT_URI = "https://activities.tjhsst.edu/ghs/login"
    AUTH_BASE_URL = "https://ion.tjhsst.edu/oauth/authorize/"
    TOKEN_URL = "https://ion.tjhsst.edu/oauth/token/"
    DEBUG = False
    app.config['APPLICATION_ROOT'] = 'activities.tjhsst.edu/ghs'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    CLIENT_ID = ""  # OAuth client ID here
    CLIENT_SECRET = ""  # OAuth client secret here
    REDIRECT_URI = ""  # OAuth redirect URI here
    AUTH_BASE_URL = "https://ion.tjhsst.edu/oauth/authorize/"
    TOKEN_URL = "https://ion.tjhsst.edu/oauth/token/"
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
