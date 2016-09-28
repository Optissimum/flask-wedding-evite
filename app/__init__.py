from flask import Flask
import flask_wtf
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'SEKRET'

# SQLAlchemy Setup
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
database = SQLAlchemy(app, session_options={'expire_on_commit': False})

from app import views, model
