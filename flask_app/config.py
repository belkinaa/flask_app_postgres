def set_config(app):
    app.config['SECRET_KEY_API'] = '0b606c7dc8323ac2f6e64efce5d65c465206a1ae8a8f14cb23'
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@127.0.0.1:5432/flask_app_db'
    return app
