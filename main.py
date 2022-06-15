import os
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))


app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{os.environ["MARIADB_USER"]}:{os.environ["MARIADB_PASSWORD"]}@{os.environ["MARIADB_SERVER"]}/{os.environ["MARIADB_DATABASE"]}'
app.secret_key = 'secret key'

db.app = app
db.init_app(app)
db.drop_all()
db.create_all()

admin = Admin(app, name='test', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

app.run()
