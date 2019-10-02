"""
Main part for running the app.
For running app in debug mode set environment variable ENV with value DEV.
Server installed by default - Development.
"""

from flask import Flask
import os

from .processing import processing

app = Flask(__name__)


def run_app():
    app.register_blueprint(processing)
    if os.environ.get('ENV') == 'DEV':
        app.config['DEBUG'] = True
    return app


run_app()
