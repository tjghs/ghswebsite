# German Honor Society Website #

## Setting up dev environment ##

* `pip install autoenv`

* Change to the project root directory, the environment should automatically activate, with a "(env)" in front of the PS1

* Run in root directory of the project
`virtualenv --no-site-packages --distribute -p python3.5 env`

* `pip install -r requirements.txt`

* Uncomment the line in app.py that says `app.config.from_object(os.environ['APP_SETTINGS'])`

* Move exampleconfig.py to config.py and add the password and url for the postgresql database, as indicated on Director

## Setting up production environment ##
* Go to `https://director.tjhsst.edu/site/12` and click on "Web Terminal"

* Run in root directory of the project (in `/public`)
`virtualenv --no-site-packages --distribute -p python3 env`

* `source env/bin/activate`

* `pip install -r requirements.txt`

* Move exampleconfig.py to config.py and add the password and url for the postgresql database, as indicated on Director
