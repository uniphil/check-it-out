#lalala

python wsgi app. and git. and together. and github. and stuff.


## Installation


Configuration is via environment variables.

## Mandatory Configuration

 * `HOST`: hostname or IP for check-it-out to run on, like 'localhost' or `0.0.0.0`. `check-it-out` will attempt to run at this hostname, and will also build the callback URL it passes to github. The callback url host can be overridden in case you are behind a reverse-proxy or something, see below the optional configuration section below.
 * `PORT`: the port to listen on, like `80` or `5000`. Same things apply as with `HOST`.
 * `APP_REPO`: the github repo of the app you want, like `uniphil/check-it-out`.
 * `APP_ROOT`: check-it-out will download your wsgi apps inside this directory.
 * `GH_CLIENT_ID`: [from github](https://github.com/settings/applications), for user authentication.
 * `GH_CLIENT_SECRET`: also [from github](https://github.com/settings/applications).
 * `SECRET_KEY`: a [secret key for flask](http://flask.pocoo.org/docs/api/#flask.Flask.secret_key) that check-it-out needs to track sessions.

## Optionl Configuration

 * `DEBUG` will enable the flask/werkzeug debugger if set to `True`.
 * `GH_CALLBACK_HOST` the public-facing host or IP for your `check-it-out` installation, which must match what you set up in your application registration [at github](https://github.com/settings/applications). `check-it-out` will use this to build the callback URL it passes to github, which is useful if you are behind a reverse-proxy or something.
 * `GH_CALLBACK_PORT` same as above


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
