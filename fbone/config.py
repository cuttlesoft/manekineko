# -*- coding: utf-8 -*-

import os

from fbone.core.utils import make_dir, INSTANCE_FOLDER_PATH


class BaseConfig(object):

    PROJECT = "fbone"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = True
    TESTING = False

    ADMINS = ['youremail@yourdomain.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'youshouldreplacethis'

    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    make_dir(LOG_FOLDER)

    # Fild upload, should override in production.
    # Limit the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'fbone/static/uploads')
    TRANSLATIONS_FOLDER = os.path.join(PROJECT_ROOT, 'fbone/translations')
    TRANSLATIONS_PATH = 'LC_MESSAGES/'
    TRANSALTIONS_FILE = 'messages.po'
    LOGO_FILE = os.path.join(PROJECT_ROOT, 'fbone/static/img/logo.png')
    make_dir(UPLOAD_FOLDER)


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # SQLITE
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/%s.sqlite' % (INSTANCE_FOLDER_PATH, BaseConfig.PROJECT)

    # MySQL
    # SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/%s?charset=utf8' % BaseConfig.PROJECT

    # PostgreSQL
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root@localhost/%s' % BaseConfig.PROJECT

    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    ACCEPT_LANGUAGES = ['zh']
    BABEL_DEFAULT_LOCALE = 'en'

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail: http://pythonhosted.org/flask-mail/
    # https://bitbucket.org/danjac/flask-mail/issue/3/problem-with-gmails-smtp-server
    MAIL_DEBUG = DEBUG
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    MAIL_USERNAME = 'gmail_username'
    MAIL_PASSWORD = 'gmail_password'
    DEFAULT_MAIL_SENDER = '%s@gmail.com' % MAIL_USERNAME

    LANGUAGES = {
        'en': 'English',
        'es': 'Español'
    }


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH + '/test.sqlite'
