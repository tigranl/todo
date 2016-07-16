from flask import Flask, request, redirect, url_for, abort, render_template, flash
from flask.ext.wtf import Form
from wtforms import TextField, StringField, PasswordField
from wtforms.validators import InputRequired, Email
from flask_mongoengine import MongoEngine
import bcrypt
from models import *

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = MongoEngine(app)


class Registration(Form):
    email = StringField('email', validators=[Email(), InputRequired()])
    first_name = StringField('first_name', validators=[InputRequired()])
    last_name = StringField('last_name', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])

    @staticmethod
    def hashing(password):
        salt = bcrypt.gensalt(12)
        password = bcrypt.hashpw(password, salt)
        return password


@app.route('/', methods=["GET", "POST"])
def reg():
    form = Registration()
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.email.data, form.first_name.data, form.last_name.data, )
        flash("You have successfully registered")

    return "sdfgsd"

if __name__ == '__main__':
    app.run()