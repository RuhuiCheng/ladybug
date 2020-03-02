import datetime
from flask_admin.contrib.sqla import ModelView
from src.www.orm import db


class EmailTemplate(db.Model):
    __tablename__ = 'email_template'
    id = db.Column(db.Integer, primary_key=True)
    email_subject = db.Column(db.String(200), unique=True)
    msg_template = db.Column((db.Text))
    email_to = db.Column(db.String(4000),nullable=False)
    email_cc = db.Column(db.String(4000),nullable=True)
    email_bcc = db.Column(db.String(4000),nullable=True)
    description = db.Column(db.String(1000),nullable=True)

    def __str__(self):
        return self.email_subject

class EmailTemplateModelView(ModelView):
    page_size = 15
    can_delete = False
