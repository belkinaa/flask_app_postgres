from flask import render_template

from flask_app import APP


@APP.route("/")
def hello_world():
    return render_template("index.html")