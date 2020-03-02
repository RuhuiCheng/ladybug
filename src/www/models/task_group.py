import datetime
from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField
from src.www.orm import db


# Define models
case_group = db.Table(
    'case_group',
    db.Column('task_case_id', db.Integer(), db.ForeignKey('task_case.id')),
    db.Column('task_group_id', db.Integer(), db.ForeignKey('task_group.id'))
)

class TaskGroup(db.Model):
    __tablename__ = 'task_group'
    id = db.Column(db.Integer, primary_key=True)
    task_group_name = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    case_list = db.relationship('src.www.models.task_case.TaskCase', secondary=case_group,
                            backref=db.backref('case_list', lazy='dynamic'))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship(
        'src.www.models.user.User', foreign_keys=[owner_id])
    is_enabled = db.Column(db.Integer)

    def __str__(self):
        return self.task_group_name


class TaskGroupModelView(ModelView):
    page_size = 15
    can_view_details = True
    can_export = True
    ls_column = ('task_group_name','description','case_list','owner','is_enabled')
    form_columns = ls_column
    column_list = ls_column
    column_searchable_list = ('task_group_name','description','is_enabled')
    form_overrides = {
        'is_enabled': SelectField
    }

    form_args = dict(
        is_enabled=dict(choices=[(1, 'yes'), (0, 'no')], coerce=int)
    )