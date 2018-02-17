from db import db

class RiskType(db.Model):
    __tablename__ = 'risk_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name
   
    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
