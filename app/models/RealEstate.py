from app import db

class RealEstate(db.Model):
    __tablename__ = 'real_estates'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    address = db.Column(db.String(255))

    def __repr__(self) -> str:
        return '<RealEstate %r>' % self.name