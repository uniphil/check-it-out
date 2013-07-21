#!/usr/bin/env python2

import tempfile
from flask import Flask
import git
from db import db


REPO_PATH = "/home/phil/Code/calama-kale"


app = Flask(__name__)


@app.route('/'):
def hello():
    return 'hey hey'


if __name__ == '__main__':
    #repo = git.Repo(REPO_PATH)
    #print "heads:\n", "\n".join("{}: {}".format(h.name, h.commit.hexsha) for h in repo.heads)
    app.run(debug=True)
