from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    
    register_blueprints(application)

    db.init_app(application)
    with application.app_context():
        # from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return application

def register_blueprints(application):
    from app.controllers import RealEstate_blueprints
    application.register_blueprint(
        RealEstate_blueprints, url_prefix='/real-estates')


config_filename = os.path.abspath(
    os.path.dirname(__file__)) + "/../instance/settings.cfg"
app = Flask(__name__)
app.config.from_pyfile(config_filename)
db = SQLAlchemy()
ma = Marshmallow(app)


#TODO: nos casos de erro, parar de renderizar o retorno como HTML

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400