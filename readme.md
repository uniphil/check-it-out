#lalala

python wsgi app. and git. and together. and github. and stuff.


## Installation

Configuration is via environment variables. You need to export the following:

 * `HOST`: hostname or IP for check-it-out to run on, like 'localhost' or `0.0.0.0`.
 * `PORT`: the port to listen on, like `80` or `5000`.
 * `APP_REPO`: the github repo of the app you want, like `uniphil/check-it-out`.
 * `APP_ROOT`: check-it-out will download your wsgi apps inside this directory.
 * `GH_CLIENT_ID`: [from github](https://github.com/settings/applications), for user authentication.
 * `GH_CLIENT_SECRET`: also [from github](https://github.com/settings/applications).
 * `SECRET_KEY`: a [secret key for flask](http://flask.pocoo.org/docs/api/#flask.Flask.secret_key) that check-it-out needs to track sessions.

`DEBUG` is the only optional environment variable, and can be `True` or `False`.

Tip: If you use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/), you can set up environment variable exports in the `postactivate` hook at `$VIRTUAL_ENV/bin/postactivate`. Mine looks like this:

```
#!/usr/bin/zsh
export HOST=0.0.0.0
export PORT=5000
export APP_REPO=uniphil/check-it-out
export APP_ROOT=/tmp/checked-out
export GH_CLIENT_ID=lalalalalalalalalala
export GH_CLIENT_SECRET=lalalalalalalalalalalalalalalalalalalala
export SECRET_KEY=lalalalalalalalalalalalalalalalalalalala
```
