#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:58:17 2018

@author: YTong
"""

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


#@ signifies a decorator
@app.route('/')
def index():
    return 'This is a homepage'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/test')
def test():
    return '<h2>Test</h2>'

#now username is a variable if inside "<>"
@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hey this is Tong</h2>'

#part2: html template
@app.route("/profile2/<name>")
def profile2(name):
    return render_template("profile")
    