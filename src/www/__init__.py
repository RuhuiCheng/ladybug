import logging
import src.utils.log
from src.utils import conf
from flask import Flask
from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
from src.www.routes.base import boot
from src.www.routes import error
import src.www.models.user as user
import src.www.models.db_connect as conn
import src.www.models.task_case as task
import src.www.models.task_group as group
import src.www.models.task_scenarios as scenarios
import src.www.models.task_execution as execution
import src.www.models.task_case_result as result
import src.www.models.email_template as email
from src.www.orm import db


def create_app():
    app = Flask(__name__)
    admin = Admin(app, name='Data Quality Platform',
                  template_mode='bootstrap3')
    # 1 setup config
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['SECRET_KEY'] = '123456789'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config = conf.init()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
        config.mysql_user, config.mysql_password, config.mysql_host, config.mysql_database)
    db.init_app(app)
    # 2 add route
    app.register_blueprint(boot)
    # 3 add model
    admin.add_view(task.TaskCaseModelView(
        task.TaskCase, task.db.session, name='Task'))
    admin.add_view(group.TaskGroupModelView(
        group.TaskGroup, group.db.session, name='Group'))
    admin.add_view(scenarios.TaskScenariosModelView(scenarios.TaskScenarios,
                                                    db.session, name='Scenarios'))
    admin.add_view(execution.TaskExecutionModelView(execution.TaskExecution,
                                                    db.session, category='Result', name='TaskExecution'))
    admin.add_view(result.TaskCaseResultModelView(
        result.TaskCaseResult, db.session, category='Result', name='TaskResult'))
    admin.add_view(user.UserModelView(user.User, db.session,
                                            category='Admin', name=u'User'))
    admin.add_view(conn.DbConnectModelView(
        conn.DbConnect, db.session, category='Admin', name='Connection'))
    admin.add_view(email.EmailTemplateModelView(
        email.EmailTemplate, db.session, category='Admin', name='Email Template'))
    # 4 error
    app.register_error_handler(Exception, error.handle_exception)
    return app
