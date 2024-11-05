#!/usr/bin/env python3
'''
basic flask app
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    '''return hello world html file'''
    return render_template('0-index.html')


if __name__ == '__main__':
    '''run'''
    app.run(debug=True)
