from app import app
from flask.ext.sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABAE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    
    def __init__(self, username):
        self.username = username
    
    def __repr__(self):
        return '<User: {}>'.format(self.username)


class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    remote = db.Column(db.String(80))

    def __init__(self, name, remote):
        self.name = name
        self.remote = remote
    
    def __repr__(self):
        return '<App: {} from {}>'.format(self.name, self.remote)
