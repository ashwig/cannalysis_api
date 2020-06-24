import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from werkzeug.utils import import_string


class CannalysisAPIConfig(object):
    DEBUG = False
    TESTING = False
    SENTRY_SECURITY_TOKEN = ''
    SENTRY_SECURITY_TOKEN_HEADER = ''
    ENV_PATH = ''
    METRC_VENDOR_KEY = ''
    METRC_USER_KEY = ''
    METRC_URI = ''
    METRC_DOCS = ''
    HOST = ''
    PORT = ''

    @property
    def HOST(self):
        return self.HOST

    @property
    def PORT(self):
        return self.PORT

    def init(self):
        self.ENV_PATH = Path('..') / '.env'
        load_dotenv(dotenv_path=self.ENV_PATH)

        self.METRC_VENDOR_KEY = os.getenv("METRC_VENDOR_KEY")
        self.METRC_USER_KEY = os.getenv("METRC_USER_KEY")
        self.METRC_URI = os.getenv("METRC_URI")
        self.METRC_DOCS = os.getenv("METRC_DOCS")


class CannalysisAPIConfigProduction(CannalysisAPIConfig):
    DEBUG = False
    TESTING = False
    HOST = 'cannalysis-api.ashwigltd.com'
    PORT = 80
    DATABASE_URI = ''
    ENV_PATH = ''

    def init(self):
        self.ENV_PATH = Path('..') / '.env.production'
        load_dotenv(dotenv_path=self.ENV_PATH)

        self.SENTRY_SECURITY_TOKEN = os.getenv("SENTRY_SECURITY_TOKEN")
        self.SENTRY_TOKEN_HEADER = os.getenv("SENTRY_TOKEN_HEADER")


class CannalysisAPIConfigDevelopment(CannalysisAPIConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'dev'
    HOST = '127.0.0.1'
    PORT = 8080


class CannalysisAPIConfigTesting(CannalysisAPIConfig):
    TESTING = True
    HOST = '127.0.0.1'
    PORT = 80
    DATABASE_URI = ''
    DATABASE_URI = ''


def create_app(test_config=None):
    cfg = import_string('CannalysisAPIConfigDevelopment')()

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_object(cfg)

    try:
        os.makedirs('app.instance_path')
    except OSError:
        pass

    @app.route("/helloworld")
    def helloworld():
        return 'Hello, world!'

    return app
