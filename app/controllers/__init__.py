from flask import Blueprint

from app.controllers.RealEstate import index as RealEstateIndex
from app.controllers.RealEstate import create as RealEstateCreate
from app.controllers.RealEstate import get as RealEstateGet
from app.controllers.RealEstate import update as RealEstateUpdate
from app.controllers.RealEstate import delete as RealEstateDelete

RealEstate_blueprints = Blueprint('real-estates', 'api')
RealEstate_blueprints.add_url_rule('/', view_func=RealEstateIndex, methods=['GET'])
RealEstate_blueprints.add_url_rule('/', view_func=RealEstateCreate, methods=['POST'])
RealEstate_blueprints.add_url_rule('/<int:id>', view_func=RealEstateGet, methods=['GET'])
RealEstate_blueprints.add_url_rule('/<int:id>', view_func=RealEstateUpdate, methods=['PUT', 'PATCH'])
RealEstate_blueprints.add_url_rule('/<int:id>', view_func=RealEstateDelete, methods=['DELETE'])