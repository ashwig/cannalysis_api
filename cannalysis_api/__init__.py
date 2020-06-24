import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from werkzeug.utils import import_string

import cannalysis_api.config as config


def create_app(test_config=None):
    cfg = config.CannalysisAPIConfigDevelopment()

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'cannalysis_api.sqlite'))

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_object(cfg)

    try:
        os.makedirs('app.instance_path')
    except OSError:
        pass

    # Initialize Database
    from . import db
    db.init_app(app)

    return app
