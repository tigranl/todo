from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from .config import *


app = Flask(__name__)
app.config.from_object(config['development'])
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'registration'
