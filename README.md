# German Honor Society Website #

* NOTE: Clone slideshow into ghswebsite/ in order for slideshow to work, otherwise it will 404.

## Setting up dev environment ##

* `pip install autoenv`

* Run in root directory of the project
`virtualenv --no-site-packages --distribute -p python3.5 env`

* Change to the project root directory, the environment should automatically activate, with a "(env)" in front of the PS1.

* `pip install -e .` will install the required packages.

* Move exampleconfig.py to config.py and add the postgresql database uri, the secret key, and other missing variables. NOTE: make sure you update config.py after changes are made to exampleconfig.py.

* Run migrations to populate the postgresql database with `python manage.py db init`, `python manage.py db migrate`, and `python manage.py db upgrade`.

* To run the development server, run `python run.py <port>`.

## Setting up production environment ##
* Go to [Director](https://director.tjhsst.edu/site/12) and click on "Web Terminal".

* Run in root directory of the project (in `/public`)
`virtualenv --no-site-packages --distribute -p python3 env`

* `pip install -e .`

* Move exampleconfig.py to config.py and add the password and url for the postgresql database, as indicated on Director.
