# -*- coding: utf-8 -*-
"""
    :original author: Grey Li (李辉)
    :modified by: Brando Zhang (大智)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.

Task 2:
    a.  Finish index.html:
            1.  User can visit /watchlist via click on the hyperlink on "watchlist" in index.html;
            3.  Make the style inherit from base.html;
    b.  Finish watchlist.html:
            1.  Use a for loop to display the watch list of the user;
            2.  Display the username;
            3.  Display the length of the watchlist;
            4.  Fix the "Return";
            5.  In Test "if", display user.bio if the user has a biography,
            otherwise it will display "This user has not provided a bio.";
    c.  Finish 404.html from an empty file (YOU CAN REFER TO 500.html)
"""

from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)


@app.route('/')
def index():
    return render_template('index.html')


# register template test
@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False


@app.route('/watchlist2')
def watchlist_with_static():
    return render_template('watchlist_with_static.html', user=user, movies=movies)


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
