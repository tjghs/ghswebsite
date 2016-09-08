from app import db
from sqlalchemy.dialects.postgresql import JSON

class Hours(db.Model):
    __tablename__ = 'hours'
    
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String())
    hours = db.Column(db.Integer, primary_key=False)
    
    def __init__(self, desc, hours):
        self.desc = desc
        self.hours = hours

    def __repr__(self):
        return '<id{}>'.format(self.id)
