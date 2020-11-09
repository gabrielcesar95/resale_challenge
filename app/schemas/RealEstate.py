from app import ma


class RealEstateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address')

    _links = ma.Hyperlinks(
        {
            'self': ma.URLFor('realestate_detail', values=dict(id='<id>')),
            'collection': ma.URLFor('realestates')
        }
    )


realestate_schema = RealEstateSchema()
realestates_schema = RealEstateSchema(many=True)
