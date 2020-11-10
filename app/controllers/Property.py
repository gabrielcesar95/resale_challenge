import json
from flask import request, jsonify, abort
from app import db
from app.models.Property import Property
from app.schemas.Property import PropertySchema, property_schema, properties_schema

schema = PropertySchema()

def index() -> dict:    
    properties: list = Property.query.order_by(Property.name).all()
    
    for property in properties:
        property.characteristics = json.loads(property.characteristics)

    return jsonify(properties_schema.dump(properties))

def create() -> dict:
    request_data = request.get_json()

    validate_errors = schema.validate(request_data)
    if(validate_errors):
        abort(400, str(validate_errors))

    characteristics = json.dumps(request_data['characteristics'])

    property = Property(
        name=request_data['name'],
        address=request_data['address'],
        description=request_data['description'],
        status=request_data['status'],
        characteristics=characteristics,
        type=request_data['type'],
        finality=request_data['finality'],
        real_estate_id=request_data['real_estate_id']
    )

    db.session.add(property)
    db.session.commit()

    property.characteristics = json.loads(property.characteristics)

    return jsonify(property_schema.dump(property))

def get(id: int) -> dict:
    property = Property.query.filter(
        Property.id == id
    ).first()

    if(property is None):
        abort(404, "Imóvel não encontrado")

    property.characteristics = json.loads(property.characteristics)

    return jsonify(property_schema.dump(property))

def update(id: int) -> dict:
    request_data = request.get_json()

    property = Property.query.filter(
        Property.id == id
    ).first()

    if(property is None):
        abort(404, "Imóvel não encontrado")

    validate_errors = schema.validate(request_data)
    if(validate_errors):
        abort(400, str(validate_errors))

    characteristics = json.dumps(request_data['characteristics'])

    property.name = request_data['name'] or property.name
    property.address = request_data['address'] or property.address
    property.description = request_data['description'] or property.description
    property.status = request_data['status'] or property.status
    property.characteristics = characteristics or property.characteristics
    property.type = request_data['type'] or property.type
    property.finality = request_data['finality'] or property.finality
    property.real_estate_id = request_data['real_estate_id'] or property.real_estate_id

    db.session.add(property)
    db.session.commit()

    property.characteristics = json.loads(property.characteristics)

    return jsonify(property_schema.dump(property))

def delete(id: int) -> dict:
    property = Property.query.filter(
        Property.id == id
    ).first()

    if(property is None):
        abort(404, "Imóvel não encontrado")

    db.session.delete(property)
    db.session.commit()

    return jsonify({
        'message': "Imóvel deletado"
    })
