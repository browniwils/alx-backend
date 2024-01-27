#!/usr/bin/env python3
"""i18n in flask"""

from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config:
    """Configuration for the babel object."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
babel.init_app(app)


@app.route("/", strict_slashes=False)
def hello_holberton():
    """Returns html template."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
