import datetime
from flask_admin.contrib.sqla import ModelView
from wtforms import TextAreaField, SelectField
from src.www.orm import db


class TaskCase(db.Model):
    __tablename__ = 'task_case'
    id = db.Column(db.Integer, primary_key=True)
    task_case_name = db.Column(db.String(1000), nullable=False, unique=True)
    alias = db.Column(db.String(1000), nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    source_sql = db.Column(db.Text, nullable=True)
    destination_sql = db.Column(db.Text, nullable=True)
    source_connect_id = db.Column(db.Integer, db.ForeignKey('db_connect.id'), nullable=True)
    source_connect = db.relationship(
        'src.www.models.db_connect.DbConnect', foreign_keys=[source_connect_id])
    destination_connect_id = db.Column(
        db.Integer, db.ForeignKey('db_connect.id'), nullable=True)
    destination_connect = db.relationship(
        'src.www.models.db_connect.DbConnect', foreign_keys=[destination_connect_id])
    is_enabled = db.Column(db.Integer,nullable=False)
    match_type = db.Column(db.Integer,nullable=False)
    threshlod_low = db.Column(db.Integer, nullable=True)
    threshlod_high = db.Column(db.Integer, nullable=True)
    duration_limit = db.Column(db.Integer)
    last_run = db.Column(db.DateTime, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship(
        'src.www.models.user.User', foreign_keys=[owner_id])
    email_template_id = db.Column(db.Integer, db.ForeignKey('email_template.id'))
    email_template = db.relationship(
        'src.www.models.email_template.EmailTemplate', foreign_keys=[email_template_id])

    def __str__(self):
        return self.task_case_name


class TaskCaseModelView(ModelView):
    page_size = 15
    can_view_details = True
    can_export = True
    ls_column = ('task_case_name', 'source_connect', 'source_sql',
                    'destination_connect', 'destination_sql',
                    'match_type', 'threshlod_low', 'threshlod_high',
                    'is_enabled', 'duration_limit', 'email_template', 'owner', 'alias','description')
    form_columns = ls_column
    column_list = ls_column
    column_searchable_list = ('task_case_name','source_sql','destination_sql','match_type','is_enabled','alias','description')

    form_overrides = {
        'source_sql': TextAreaField,
        'destination_sql': TextAreaField,
        'is_enabled': SelectField,
        'match_type': SelectField
    }

    form_args = dict(
        is_enabled=dict(choices=[(1, 'yes'), (0, 'no')], coerce=int),
        match_type=dict(choices=[(2, 'range'), (1, 'exactly')], coerce=int)
    )
