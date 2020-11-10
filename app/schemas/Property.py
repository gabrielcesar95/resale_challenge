from app.models.RealEstate import RealEstate
from marshmallow import Schema, fields
from marshmallow.validate import *
from app import db

class PropertySchema(Schema):
    name = fields.Str(required=True, allow_none=False, validate=Length(min=1, max=120))
    address = fields.Str(required=True, allow_none=False, validate=Length(min=1, max=255))
    description = fields.Str(required=True, allow_none=False, validate=Length(min=1, max=1200))
    status = fields.Boolean(required=True, allow_none=False)
    characteristics = fields.Dict(keys=fields.Str(), values=fields.Int())
    type = fields.Str(validate=OneOf(['H', 'A']))
    finality = fields.String(validate=OneOf(['R', 'B']))
    real_estate_id = fields.Int(required=True, validate=lambda x: real_estate_exists(x, RealEstate))

    class Meta:
        fields = ('id', 'name', 'address', 'description', 'status', 'characteristics', 'type', 'finality', 'real_estate_id')

def real_estate_exists(id, model):
    if not db.session.query(db.exists([model.id]).where(model.id == id)).scalar():
        raise ValidationError('%s ID: %i does not exist' % (model, id))

property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)
