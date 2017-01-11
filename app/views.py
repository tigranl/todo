from app import app, login_manager
from flask import request, redirect, url_for, render_template, g
from flask.ext.login import login_user, current_user

from .models import User, Note
from .forms import *


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except:
        return None


@app.before_request
def before_request():
    g.user = current_user


def notes():
    posts = Note.objects.filter(author=g.user.id)
    post_form = Post()
    if request.method == 'POST' and post_form.validate_on_submit():
        print(g.user.email)
        post = Note(note=post_form.title.data)
        post.author.append(g.user._get_current_object())
        post.save()
        return redirect(url_for('login'))

    return render_template('tasks.html', post_form=post_form, posts=posts)


@app.route('/notes', methods=["GET", "POST"])
def registration():
    form = Registration()
    if request.method == 'POST' and form.validate_on_submit():
        user = User(email=form.email.data, first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    password=form.hashing(form.password.data.encode('utf-8')))
        user.save()
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)


@app.route('/', methods=["GET", "POST"])
def login():
    if g.user is not None and g.user.is_authenticated:
        return notes()
    else:
        login_form = Login()
        if request.method == 'POST' and login_form.validate_on_submit():
            if login_form.checkbox:
                remember_me = True
            try:
                user = User.objects.get(email=login_form.email.data)
                form_data = login_form.password.data.encode('utf-8')
                if user and bcrypt.hashpw(form_data, user.password) \
                        == user.password:
                    login_user(user, remember=remember_me)
                    return notes()
                else:
                    return "Check your email and password and try again"
            except:
                    return "Error occurred"
        return render_template('login.html', login_form=login_form)
