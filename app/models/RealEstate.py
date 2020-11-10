from app.models.Property import Property
from app import db
from sqlalchemy.orm import relationship

class RealEstate(db.Model):
    __tablename__ = 'real_estates'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    address = db.Column(db.String(255))
    properties = relationship(Property)

    def __repr__(self) -> str:
        return '<RealEstate %r>' % self.name