from flask import request, jsonify

# from app.models import RealEstate


def index() -> dict:
    real_estates = [
        {
            'id': 1,
            'name': 'Frias Neto'
        },
        {
            'id': 2,
            'name': 'Ato'
        },
    ]
    return {'data': real_estates}


def create() -> dict:
    real_estate = {
        'name': request.json.get('name')
    }


    return real_estate

def get(id: int) -> dict:
    real_estate = {
        'id': id,
        'name': 'Alguma Imobiliária'
    }
    return real_estate

def update(id: int) -> dict:
    real_estate = {
        'id': id,
        'name': 'Alguma Imobiliária (alterada)'
    }
    return real_estate

def delete(id: int) -> dict:
    deleted_item = {
        'message': 'deleted successfully',
        'id': id
    }
    return deleted_item
