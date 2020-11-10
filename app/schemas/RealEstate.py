from marshmallow import Schema, fields
from marshmallow.validate import *

class RealEstateSchema(Schema):
    name = fields.Str(required=True, allow_none=False, validate=Length(min=1, max=120))
    address = fields.Str(validate=Length(max=255))
    class Meta:
        fields = ('id', 'name', 'address')


realestate_schema = RealEstateSchema()
realestates_schema = RealEstateSchema(many=True)
