#!/usr/bin/env python2

from checkitout import app

if __name__  == '__main__':
    app.config['SECRET_KEY'] = 'a terrible key'
    app.run(debug=True)
