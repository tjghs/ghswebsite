import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


print(os.environ['APP_SETTINGS'])


from models import Hours


@app.route("/")
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
