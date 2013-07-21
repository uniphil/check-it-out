from flask.ext.wtf import Form
from wtforms import TextField, PasswordField


class LoginForm(Form):
    username = TextField("username")
    password = PasswordField("password")
