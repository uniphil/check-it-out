#!/usr/bin/env python2

import git

from flask import Flask, render_template
app = Flask(__name__)

from flask.ext.login import LoginManager
login_manager = LoginManager(app)

import gh
from db import db
import endpoints


REPO_PATH = "/home/phil/Code/calama-kale"


#repo = git.Repo(REPO_PATH)
#print "heads:\n", "\n".join("{}: {}".format(h.name, h.commit.hexsha) for h in repo.heads)
