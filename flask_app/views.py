from flask_app import APP


@APP.route("/")
def hello_world():
    return "<p>Hello, World!</p>"