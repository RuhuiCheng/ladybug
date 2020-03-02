import datetime
from flask_admin.contrib.sqla import ModelView
from src.www.orm import db


class TaskCaseResult(db.Model):
    __tablename__ = 'task_case_result'
    id = db.Column(db.Integer, primary_key=True)
    task_case_id = db.Column(db.Integer)
    task_execution_id = db.Column(db.Integer)
    current_status = db.Column(db.String(50))
    execution_start = db.Column(db.DateTime, nullable=True)
    execution_end = db.Column(db.DateTime, nullable=True)
    source_result = db.Column(db.Text)
    destination_result = db.Column(db.Text)
    diff = db.Column(db.Text)
    result_message = db.Column(db.Text)


class TaskCaseResultModelView(ModelView):
    page_size = 15
    can_create = False
    can_edit = False
    can_delete = False
    column_searchable_list = ['source_result',
                              'destination_result','diff', 
                              'result_message','current_status']
    column_filters = ['execution_start', 'execution_end']
