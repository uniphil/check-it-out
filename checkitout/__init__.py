#!/usr/bin/env python2

from flask import Flask, render_template
app = Flask(__name__)

from flask.ext.login import LoginManager
login_manager = LoginManager(app)

import config
import repository
from db import db
import endpoints
