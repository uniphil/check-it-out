#!/usr/bin/env python2
"""
    checkitout.py
    ~~~~~~~~~~~~~

    Pull python wsgi apps from github. See readme.md.
"""

from os import environ as env
from requests import post
from werkzeug import url_encode
from github3 import login as gh_from_login
from flask import (Flask, request, session, url_for, redirect, render_template,
                   flash, abort)
from flask.ext.login import (LoginManager, login_required, UserMixin, 
                             login_user, logout_user, current_user)

app = Flask(__name__)
login_manager = LoginManager(app)

try:
    app.config.update(DEBUG=env.get('DEBUG', 'False')=='True',
                      HOST=env['HOST'], PORT=env['PORT'],
                      SECRET_KEY=env['SECRET_KEY'])
except KeyError as e:
    e.message += "check-it-out must be configured with environment "\
                 "variables.\n See readme.md."
    raise e


@app.route('/')
def hello():
    if not current_user.is_authenticated():
        return render_template('hello.html')
    return render_template('home.html')


@app.route('/login')
@login_manager.unauthorized_handler
def login():
    gh_auth_url = 'https://github.com/login/oauth/authorize'
    redirect_uri = '{}:{}{}'.format(env.get('GH_CALLBACK_HOST', env['HOST']),
                                    env.get('GH_CALLBACK_PORT', env['PORT']),
                                    url_for('oauth_callback'))
    auth_request_query = url_encode({'client_id': env['GH_CLIENT_ID'],
                                     'redirect_uri': redirect_uri,
                                     'scope': 'repo'})
    app_auth_url = '{}?{}'.format(gh_auth_url, auth_request_query)
    return redirect(app_auth_url)


@app.route('/post-auth')
def oauth_callback():
    # Get the access token
    gh_access_url = 'https://github.com/login/oauth/access_token'
    access_request_data = dict(client_id=app.config['GH_CLIENT_ID'],
                               client_secret=app.config['GH_CLIENT_SECRET'],
                               code=request.args['code'])
    gh_access = post(gh_access_url, data=access_request_data,
                     headers={'accept': 'application/json'})
    access_token = access_stuff.json().get('access_token')
    assert access_token is not None, "no access token provided..."

    # Now get YOU!!!
    user = RepoUser.get(access_token)

    # Get the repo...
    repo_user, repo_name = env['APP_REPO'].split('/', 1)
    gh_repo = user.gh.repository(repo_user, repo_name)
    if gh_repo is None:
        flash("Can\'t find that repo on GitHub for you. Do you have access?")
        abort(404)

    # Check access...
    if not gh_repo.is_collaborator(gh_user.login):
        abort(403)  # :(

    # All good!
    login_user(user, remember=True)
    return redirect(url_for('hello'))


class RepoUser(UserMixin):
    """A user on GitHub with collaborator access to our repo."""
    def __init__(self, gh):
        self.gh = gh
        self._gh_user = gh.user()

    def __getattr__(self, name):
        """Defer stuff we don't have to our github3 user instance."""
        return getattr(self._gh_user, name)

    @classmethod
    def get(cls, access_code):
        gh = gh_from_login(token=access_token)
        return cls(gh)


@app.errorhandler(403)
def sadface(error):
    return render_template('403-unauthorized.html'), 403


@app.errorhandler(401)
def ohnoes(error):
    return render_template('404-whaaaaat.html'), 404


if __name__ == '__main__':
    app.run(host=app.config['HOST'])  # ugh. I guess it makes sense that host
                                      # has to be set here...
