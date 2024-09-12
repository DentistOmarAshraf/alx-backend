#!/usr/bin/env python3
"""
Flask app - Using Babel
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, format_datetime
from datetime import datetime
import pytz
from typing import Any, Dict

import pytz.exceptions


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_id: int = None) -> Dict:
    """get_user
    """
    if not login_id:
        return None
    return users.get(login_id, None)


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


@app.before_request
def before_request() -> None:
    """Getting user id from args
    """
    user_id = request.args.get('login_as', None)
    if user_id:
        the_user = get_user(int(user_id))
    else:
        the_user = None
    g.user = the_user


@babel.localeselector
def get_locale() -> Any:
    """preferd language from request header (Accept Language)
    """
    lang = request.args.get('locale', None)
    the_user = getattr(g, 'user', None)

    if lang and lang in Config.LANGUAGES:
        return lang
    if the_user:
        user_lang = the_user.get('locale', None)
        if user_lang in Config.LANGUAGES:
            return user_lang
    return request.accept_languages.best_match(Config.LANGUAGES)

@babel.timezoneselector
def get_timezone() -> Any:
    """User time zone
    """
    time_zone = request.args.get('timezone', None)
    the_user = getattr(g, 'user', None)
    if time_zone:
        try:
            datetime_zone = datetime.now(pytz.timezone(time_zone))
            return time_zone
        except pytz.exceptions.UnknownTimeZoneError as e:
            pass
    if the_user:
        try:
            datetime_zone = datetime.now(pytz.timezone(the_user['timezone']))
            return the_user['timezone']
        except pytz.exceptions.UnknownTimeZoneError as e:
            pass
    return Config.BABEL_DEFAULT_TIMEZONE



@app.route("/", strict_slashes=False, methods=['GET'])
def home() -> Any:
    """index page
    """
    the_user = getattr(g, 'user', None)
    time_now = format_datetime(datetime.now())
    if the_user:
        username = the_user.get('name', None)
    else:
        username = None
    return render_template("7-index.html",
                            username=username,
                            time_now=time_now)


if __name__ == "__main__":
    """Main"""
    app.run(host='0.0.0.0', port=5000)
