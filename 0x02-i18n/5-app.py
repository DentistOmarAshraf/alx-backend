#!/usr/bin/env python3
"""
Flask app - Using Babel
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Any, Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    the_user = getattr(g, 'user', None)
    if the_user:
        prefered_lang = the_user.get('locale', None)
    else:
        prefered_lang = None
    if prefered_lang and prefered_lang in Config.LANGUAGES:
        return prefered_lang
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.before_request
def get_user() -> None:
    """Getting user id from args
    """
    user_id = request.args.get('login_as', None)
    if user_id:
        the_user = users.get(int(user_id), None)
    else:
        the_user = None
    g.user = the_user


@app.route("/", strict_slashes=False, methods=['GET'])
def home() -> Any:
    """index page
    """
    the_user = getattr(g,'user', None)
    if the_user:
        return render_template("5-index.html", username=the_user.get('name', None))
    return render_template("5-index.html", username=None)


if __name__ == "__main__":
    """Main"""
    app.run(host='0.0.0.0', port=5000)
