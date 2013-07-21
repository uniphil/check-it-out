from flask import request, render_template, url_for, redirect
from flask.ext.login import login_user, logout_user, login_required
from . import app
from .forms import LoginForm
from db import User

@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(User("abcd"), remember=True)
        return redirect(request.args.get("next") or url_for("hello"))
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('hello'))


@app.route('/account')
@login_required
def account():
    return "hey you"
