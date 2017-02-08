#!/usr/bin/python3
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Hour(db.Model):
    __tablename__ = "hours"

    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean)
    desc = db.Column(db.String(140))
    hours = db.Column(db.Integer)
    date = db.Column(db.Date)
    item = db.Column(db.Boolean) #if item that can be counted as hour

    def __init__(self, admin, desc, hours, date, item):
        self.admin = admin
        self.desc = desc
        self.hours = hours
        self.date = date
        self.item = item

    def __repr__(self):
        return "<id{}>".format(self.id)


class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    tag = db.Column(db.String(10))
    desc = db.Column(db.String(140))
    date = db.Column(db.Date)

    def __init__(self, title, tag, desc, date):
        self.title = title
        self.tag = tag
        self.desc = desc
        self.date = date

    def __repr__(self):
        return "<id{}>".format(self.id)
