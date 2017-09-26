# German Honor Society Website #

## Setting up dev environment ##

* Run in root directory of the project
`virtualenv --no-site-packages --distribute -p python3.5 env`

* Change to the project root directory, the environment should automatically activate, with a "(env)" in front of the PS1.

* `pip install -e .` will install the required packages.

* Set up OAuth on [Ion](https://ion.tjhsst.edu/oauth)

* Run migrations with `python manage.py migrate`

* Run development server with `python manage.py runserver <port>`

* Copy `ghswebsite/settings/secret.py.example` to `ghswebsite/settings/secret.py`
    * Fill in the fields for Client ID and Client secret.
    * Debug mode should be `True`

## Setting up production environment ##
* TODO
