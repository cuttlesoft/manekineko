# -*- coding: utf-8 -*-
"""
    fbone.core.extensions
    ~~~~~~~~~~~~~~~~

    flask extension initializations
"""

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.migrate import Migrate
migrate = Migrate()

from flask.ext.mail import Mail
mail = Mail()

from flask.ext.cache import Cache
cache = Cache()

from flask.ext.login import LoginManager
login_manager = LoginManager()

# add redis here
