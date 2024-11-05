#!/usr/bin/env python3
'''Flask babel'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''return locale'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''return hello world html file'''
    return render_template('3-index.html')


if __name__ == '__main__':
    '''run'''
    app.run(debug=True)
