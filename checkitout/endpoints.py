from flask import request, render_template, url_for, redirect
from flask.ext.login import current_user, login_user, logout_user, login_required
from . import app
from .forms import LoginForm
from db import User

@app.route("/")
def hello():
    if current_user.is_authenticated():
        from .repository import repo
        return render_template("home.html", repo=repo)
    return redirect(url_for('login'))


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
