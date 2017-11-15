"""rmon.app

the model app create function
"""

import os
from flask import Flask

from rmon.views import api
from rmon.models import db
from rmon.config import DevConfig, ProductConfig


def create_app():
    """
    create an initiaze flask app
    """
    app = Flask("rmon")

    env = os.environ.get('RMON_ENV')

    if env in ('pro','prod','product'):
        app.config.from_object(ProductConfig)
    else:
        app.config.from_object(DevConfig)

    app.config.from_envvar('RMON_SETTINGS',silent=True)

<<<<<<< HEAD
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
=======
    app.config('SQLALCHEMY_TRACK_MODIFICATIONS') = False
>>>>>>> 173f57df2351035151f3c6b43477a1ab2dd55556

    app.register_blueprint(api)

    db.init_app(app)

    if app.debug:
        with app.app_context():
<<<<<<< HEAD
            db.create_all()
=======
            db.createall()
>>>>>>> 173f57df2351035151f3c6b43477a1ab2dd55556
        return app

