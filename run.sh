#!/bin/sh
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
export FLASK_APP=/web/activities/ghs/public/ghswebsite/app.py
export APP_SETTINGS="config.ProductionConfig"
/web/activities/ghs/public/env/bin/flask run -p $PORT

#/web/activities/ghs/public/env/bin/python /web/activities/ghs/public/ghswebsite/app.py $PORT
