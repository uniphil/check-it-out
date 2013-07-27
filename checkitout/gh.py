from . import app, login_manager
from flask.ext.login import UserMixin
from github3 import login


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    admin = db.Column(db.Boolean())
    username = db.Column(db.String(80), unique=True)
    access_token = db.Column(db.String(40))

    @classmethod
    def get(cls, id):
        "la la la"
        db_id = int(id)
        return cls.query.get(db_id)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


@login_manager.user_loader
def load_user(userid):
    return User.get(userid)
