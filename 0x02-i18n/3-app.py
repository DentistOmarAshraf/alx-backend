#!/usr/bin/env python3
"""
Flask app - Using Babel
"""
from flask import Flask, request, render_template
from flask_babel import Babel
from typing import Any


class Config:
    """
    App Config
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Any:
    """preferd language from request header (Accept Language)
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", strict_slashes=False, methods=['GET'])
def home() -> Any:
    """index page
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    """Main"""
    app.run(host='0.0.0.0', port=5000)
