#!/usr/bin/env python3
"""
Flask web app - Using Babel
"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import Any


class Config:
    """
    flask app configs
    """
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False, methods=['GET'])
def home() -> Any:
    """index
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    """Main
    """
    app.run(host='0.0.0.0', port=5000)
