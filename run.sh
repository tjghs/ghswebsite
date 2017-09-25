#!/bin/sh
cd /web/activities/ghs/public
env/bin/python ghswebsite/manage.py runserver $PORT
#/web/activities/ghs/public/env/bin/python /web/activities/ghs/public/ghswebsite/app.py $PORT
