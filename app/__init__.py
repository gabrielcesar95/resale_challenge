from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    initialize_extensions(application)
    register_blueprints(application)
    return application


def initialize_extensions(application):
    #from app.models.RealEstate import RealEstate
    #from app.models.Property import Property

    db = SQLAlchemy(application)


def register_blueprints(application):
    from app.controllers import RealEstate_blueprints
    application.register_blueprint(RealEstate_blueprints, url_prefix='/real-estates')


config_filename = os.path.abspath(
    os.path.dirname(__file__)) + "/../instance/settings.cfg"
app = Flask(__name__)
app.config.from_pyfile(config_filename)
db = SQLAlchemy(app)
