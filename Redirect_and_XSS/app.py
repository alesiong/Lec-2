# -*- coding: utf-8 -*-
"""
Task 1:
    a.  Visit http://127.0.0.1/, and then visit http://127.0.0.1/set/<type your name here> to set a cookie.
        When you revisit http://127.0.0.1/, the website still remembers your name.
    b.  Complete hi() so that when user visits http://127.0.0.1/hi, it will be redirect to http://127.0.0.1/hello.
    c.  Implement XSS via URL. (It may fails on Safari and Chrome, I will use Firefox to show)
    d.  Fix this XSS loophole in hello().
    optional:   Design your own set_cookie and corresponding view functions by referring the following programs.
"""

from jinja2 import escape
from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__)


# set cookie
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


"""
Incomplete programs start from here
"""


@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    response = '<h1>Hello, %s!</h1>' % escape(name)
    return response


@app.route('hi')
def hi():
    return redirect(url_for('hello'))
