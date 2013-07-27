#!/usr/bin/env python2
"""
    checkitout.py
    ~~~~~~~~~~~~~

    Pull python wsgi apps from github. See readme.md.
"""

from os import environ as env
from werkzeug import url_encode
from github3 import login
from flask import Flask, session, url_for, redirect, render_template
from flask.ext.login import (LoginManager, login_required, UserMixin, 
                             login_user, logout_user)

app = Flask(__name__)
try:
    app.config.update(DEBUG=env.get('DEBUG', 'False')=='True',
                      HOST=env['HOST'], PORT=env['PORT'])
except KeyError as e:
    e.message += "check-it-out must be configured with environment "\
                 "variables.\n All are mandatory. See readme.md."
    raise e



if __name__ == '__main__':
    app.run()
