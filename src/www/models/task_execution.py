import datetime
from flask_admin.contrib.sqla import ModelView
from src.www.orm import db


class TaskExecution(db.Model):
    __tablename__ = 'task_execution'
    id = db.Column(db.Integer, primary_key=True)
    execution_type = db.Column(db.String(50))
    execution_name = db.Column(db.String(1000))
    current_status = db.Column(db.String(50))
    execution_start = db.Column(db.DateTime, nullable=True)
    execution_end = db.Column(db.DateTime, nullable=True)


class TaskExecutionModelView(ModelView):
    page_size = 15
    can_create = False
    can_edit = False
    can_delete = False
    column_searchable_list = ['execution_type','execution_name','current_status']
    column_filters = ['execution_start','execution_end']