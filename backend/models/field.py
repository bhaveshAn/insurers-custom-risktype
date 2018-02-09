from db import db
from models.risk_type import RiskType

class Field(db.Model):
    __tablename__ = 'field'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))
    value = db.Column(db.String(255))
    risk_type_id = db.Column(db.Integer, db.ForeignKey('risk_type.id'))


    def __init__(self, name, _type, value, risk_type_id):
        self.id = None
        self.name = name
        self.value = value
        self.type = _type
        self.risk_type_id = risk_type_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'risk_type_id': self.risk_type_id
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
