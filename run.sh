#!/bin/sh
cd /web/activities/ghs/public/ghswebsite
/web/activities/ghs/public/env/bin/gunicorn ghswebsite.wsgi -b 127.0.0.1:$PORT -w=15
