from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email
import bcrypt


class Registration(Form):
    email = StringField('email', validators=[Email(), InputRequired()])
    first_name = StringField('first_name', validators=[InputRequired()])
    last_name = StringField('last_name', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('Sign up')

    @staticmethod
    def hashing(password):
        salt = bcrypt.gensalt(12)
        password = bcrypt.hashpw(password, salt)
        return password


class Login(Form):
    email = StringField(validators=[Email(), InputRequired()],
                        render_kw={'id': 'email', 'class': 'validate',
                                   'type': 'email'})
    password = PasswordField(validators=[InputRequired()],
                             render_kw={'id': 'password', 'class': 'validate',
                                        'type': 'password'})
    submit = SubmitField('Login', render_kw={'class': 'waves-effect waves-light btn'})
    checkbox = BooleanField(render_kw={'class': 'filled-in', 'id': 'filled-in-box'})


class Post(Form):
    title = StringField(validators=[InputRequired()])
    submit = SubmitField('Add note')
