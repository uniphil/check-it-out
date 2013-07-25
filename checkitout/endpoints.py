from werkzeug import url_fix, url_encode
from flask import request, render_template, url_for, redirect
from flask.ext.login import current_user, login_user, logout_user, login_required
from . import app
from .forms import LoginForm
from gh import db, User


def ext_url(url, **url_args):
    ext = url_fix(url)
    if url_args:
        encoded = url_encode(url_args)
        ext += "?{}".format(encoded)
    return ext


@app.route("/")
@login_required
def hello():
    return render_template("home.html", repo="lalala")


@app.route("/login")
def login():
    if 'code' not in request.args:
        return redirect(ext_url(app.config['GH_OAUTH_URL'],
                               client_id=app.config['GH_CLIENT_ID'],
                               redirect_uri='http://checkit.u24.ca:5000/login',
                               scope='user:email,repo'))
    # hello github! lets grab our access token...
    from requests import post
    access_data = dict(client_id=app.config['GH_CLIENT_ID'],
                       client_secret=app.config['GH_CLIENT_SECRET'],
                       code=request.args['code'])
    access_stuff = post(app.config['GH_OAUTH_ACCESS_URL'],
                        data=access_data,
                        headers={'accept': 'application/json'})
    access_token = access_stuff.json().get('access_token')
    assert access_token is not None, "no access token provided..."
    # ok, now get the user...
    from github3 import login
    gh = login(token=access_token)
    gh_user = gh.user()
    user = User.query.filter_by(username=gh_user.login).first()
    if user is None:
        user = User(gh_user.login, gh_user.name, access_token)
        db.session.add(user)
        db.session.commit()
    login_user(user, remember=True)
    return redirect(url_for('hello'))
