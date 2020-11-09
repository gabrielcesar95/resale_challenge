from flask import request, jsonify, abort
from app import db
from app.models.RealEstate import RealEstate
from app.schemas.RealEstate import RealEstateSchema, realestate_schema, realestates_schema

schema = RealEstateSchema()
request_data = request.get_json()

def index() -> dict:
    real_estates:list = RealEstate.query.order_by(RealEstate.name).all()

    return jsonify(realestates_schema.dump(real_estates))

def create() -> dict:
    validate_errors = schema.validate(request_data)
    if(validate_errors):
        abort(400, str(validate_errors))

    real_estate = RealEstate(
        name = request_data['name'],
        address = request_data['address'])

    db.session.add(real_estate)
    db.session.commit()

    return jsonify(realestate_schema.dump(real_estate))

def get(id: int) -> dict:
    real_estate = RealEstate.query.filter(
        RealEstate.id == id
    ).first()

    if(real_estate is None):
        abort(404, "Imobiliária não encontrada")

    return jsonify(realestate_schema.dump(real_estate))

def update(id: int) -> dict:
    real_estate = RealEstate.query.filter(
        RealEstate.id == id
    ).first()

    if(real_estate is None):
        abort(404, "Imobiliária não encontrada")

    validate_errors = schema.validate(request_data)
    if(validate_errors):
        abort(400, str(validate_errors))

    real_estate.name = request_data['name'] or real_estate.name
    real_estate.address = request_data['address'] or real_estate.address
    
    db.session.add(real_estate)
    db.session.commit()

    return jsonify(realestate_schema.dump(real_estate))

def delete(id: int) -> dict:
    real_estate = RealEstate.query.filter(
        RealEstate.id == id
    ).first()

    if(real_estate is None):
        abort(404, "Imobiliária não encontrada")

    db.session.delete(real_estate)
    db.session.commit()

    return jsonify({
        'message': "Imobiliária deletada"
    })