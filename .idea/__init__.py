from flask import Flask, request, redirect, url_for, render_template
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
import bcrypt
from models import *
from config import *
from flask.ext.login import LoginManager, login_user, current_user, AnonymousUserMixin

app = Flask(__name__)
app.config.from_object(config['development'])
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
login_manager = LoginManager()
login_manager.anonymous_user = Anonymous
login_manager.init_app(app)
