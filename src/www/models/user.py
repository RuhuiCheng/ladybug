import datetime
from flask_admin.contrib.sqla import ModelView
from src.www.orm import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    mobile = db.Column(db.String(20))

    def __str__(self):
        return self.email

class UserModelView(ModelView):
    page_size = 15