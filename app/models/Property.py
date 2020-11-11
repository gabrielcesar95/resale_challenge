import enum
from app import db
from sqlalchemy import ForeignKey

class PropertyType(enum.Enum):
    H = 'House'
    A = 'Apartment'

class PropertyFinality(enum.Enum):
    R = 'Residence'
    B = 'Business'

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    address = db.Column(db.String(255))
    description = db.Column(db.String(1200))
    status = db.Column(db.Boolean)
    characteristics = db.Column(db.Text())
    type = db.Column(db.Enum(PropertyType))
    finality = db.Column(db.Enum(PropertyFinality))
    real_estate_id = db.Column(db.Integer, ForeignKey('real_estates.id', ondelete='CASCADE'))

    def __repr__(self) -> str:
        return '<Property %r>' % self.name

