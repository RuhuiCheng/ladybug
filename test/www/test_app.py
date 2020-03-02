from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
 # 1 setup config
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = '123456789'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/data_quality'
db = SQLAlchemy(app)


# # Define models
# task_conn = db.Table(
#     'task_conn',
#     db.Column('task_case_id', db.Integer(), db.ForeignKey('task_case.id')),
#     db.Column('db_connect_id', db.Integer(), db.ForeignKey('db_connect.id'))
# )


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


class TaskCase(db.Model):
    __tablename__ = 'task_case'
    id = db.Column(db.Integer, primary_key=True)
    task_case_name = db.Column(db.String(1000), unique=True)
    alias = db.Column(db.String(1000), nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    source_sql = db.Column(db.Text, nullable=True)
    # source_connect_id = db.Column(db.Integer, nullable=True, default=0)
    # source_connect = db.relationship('DbConnect', secondary=task_conn,
    #                         backref=db.backref('conns', lazy='dynamic'))
    destination_sql = db.Column(db.Text, nullable=True)
    destination_connect_id = db.Column(db.Integer, db.ForeignKey('db_connect.id'))
    destination_connect = db.relationship('DbConnect')
    is_enabled = db.Column(db.Integer)
    match_type = db.Column(db.Integer)
    threshlod_low = db.Column(db.Integer, nullable=True)
    threshlod_high = db.Column(db.Integer, nullable=True)
    duration_limit = db.Column(db.Integer)
    last_run = db.Column(db.DateTime, nullable=True)
    owner_id = db.Column(db.Integer)
    dq_email_id = db.Column(db.Integer)
    
    def __str__(self):
        return self.task_case_name


admin = Admin(app, name='Data Quality Platform',
                  template_mode='bootstrap3')

admin.add_view(ModelView(DbConnect, db.session))
admin.add_view(ModelView(TaskCase, db.session))

if __name__ == "__main__":
    app.run(debug=True)