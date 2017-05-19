#!/bin/sh
export FLASK_APP=/web/activities/ghs/public/ghswebsite/app.py
export APP_SETTINGS="config.ProductionConfig"
/web/activities/ghs/public/env/bin/flask run -p $PORT
