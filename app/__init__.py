from flask import Flask

from app import config

from app.extensions.db import db

from app.routes import info


def create_app():

    app = Flask(__name__)

    config.start(app)

    db.init_app(app)

    info.start(app)

    return app
