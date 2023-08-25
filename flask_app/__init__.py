
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_app.config import set_config


db = SQLAlchemy()

APP = Flask(__name__)
APP = set_config(APP)


db.init_app(APP)


from flask_app.models_db import Users

with APP.app_context():
    db.create_all()

from flask_app.views import *