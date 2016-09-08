from app import db
from sqlalchemy.dialects.postgresql import JSON

class Hours(db.Model):
    __tablename__ = 'hours'
    
    id = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, hours):
        self.hours = hours

    def __repr__(self):
        return '<id{}>'.format(self.id)
