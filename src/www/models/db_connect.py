import datetime
from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField
from src.www.orm import db


class DbConnect(db.Model):
    __tablename__ = 'db_connect'
    id = db.Column(db.Integer, primary_key=True)
    db_connect_name = db.Column(db.String(200), unique=True)
    db_connect_type = db.Column(db.Integer)
    host = db.Column(db.String(200))
    port = db.Column(db.Integer)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    db_name = db.Column(db.String(200))

    def __str__(self):
        return self.db_connect_name


class DbConnectModelView(ModelView):
    page_size = 15
    can_view_details = True
    can_delete = False

    form_overrides = {
        "db_connect_type": SelectField
    }

    form_args = dict(
        db_connect_type=dict(
            choices=[(1, 'hive'), (2, 'mysql'), (3, 'oracle')],
            coerce=int)
    )
