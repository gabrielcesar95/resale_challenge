from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)

    application.register_error_handler(400, bad_request)
    application.register_error_handler(404, resource_not_found)
    
    register_blueprints(application)

    db.init_app(application)
    with application.app_context():
        db.create_all()  # Create sql tables for our data models

        return application

def register_blueprints(application):
    from app.controllers import RealEstate_blueprints
    from app.controllers import Property_blueprints

    application.register_blueprint(
        RealEstate_blueprints, url_prefix='/real-estates')
    application.register_blueprint(
        Property_blueprints, url_prefix='/properties')

config_filename = os.path.abspath(
    os.path.dirname(__file__)) + "/../instance/settings.cfg"
app = Flask(__name__)
app.config.from_pyfile(config_filename)
db = SQLAlchemy()
ma = Marshmallow(app)


@app.errorhandler(400)
def bad_request(e):
    return_payload = {
        'errors':e.description
    }
    return jsonify(return_payload), 400

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
