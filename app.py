#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    books=[
        {'title':'Python Basics','author':'Al Sweigart'},
        {'title':'Python Tricks','author':'Dan Bader'},
        {'title':'Flask Web Development','author':'Miguel Grinberg'}
    ]
    return render_template('index.html',books=books)

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run()