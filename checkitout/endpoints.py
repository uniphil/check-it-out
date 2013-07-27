from werkzeug import url_fix, url_encode
from flask import request, render_template, url_for, redirect
from flask.ext.login import current_user, login_user, logout_user, login_required
from . import app
from .appserver import app_url
from gh import db, User


def ext_url(url, **url_args):
    ext = url_fix(url)
    if url_args:
        encoded = url_encode(url_args)
        ext += "?{}".format(encoded)
    return ext


@app.route("/")
def hello():
    if not current_user.is_authenticated():
        return render_template("hello.html")
    repos = current_user.gh.iter_user_repos(current_user.gh.user().login, number=5)
    return render_template("home.html", repos=repos, app_url=app_url, dir=dir)
    


@app.route("/login")
def login():
    if 'code' not in request.args:
        return redirect(ext_url(app.config['GH_OAUTH_URL'],
                               client_id=app.config['GH_CLIENT_ID'],
                               redirect_uri='{}/login'.format(app.config['HOSTPORT']),
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
    login_user(user, remember=True)
    return redirect(url_for('hello'))


@app.route('/settings')
@login_required
def settings():
    return 'you are so cool.'


@app.route('/logout')
def logout():
    logout_user()
    return render_template('logged_out.html')
