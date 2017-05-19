#!/bin/sh
source .productionenv
env/bin/flask run -p $PORT
