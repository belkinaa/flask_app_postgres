from flask_app import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.INTEGER, primary_key=True)
    email = db.Column(db.TEXT, unique=True, nullable=False)


    def __repr__(self):
        return f"{self.__tablename__}: {self.id},{self.email}"