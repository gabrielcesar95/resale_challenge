from flask import request, jsonify, abort
from app import db
from app.models.RealEstate import RealEstate
from app.schemas.RealEstate import realestate_schema, realestates_schema


def index() -> dict:
    real_estates:list = RealEstate.query.order_by(RealEstate.name).all()

    return jsonify(realestates_schema.dump(real_estates))

def create() -> dict:
    name = request.json.get('name')
    address = request.json.get('address')

    real_estate = RealEstate(name = name, address = address)

    # TODO: Adicionar validações antes de salvar
    db.session.add(real_estate)
    db.session.commit()

    return jsonify(real_estate.as_dict())

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

    real_estate.name = request.json.get('name') or real_estate.name
    real_estate.address = request.json.get('address') or real_estate.address

    # TODO: Adicionar validações antes de salvar
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