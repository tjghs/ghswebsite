#!/usr/bin/python3
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Hour(db.Model):
    __tablename__ = "hours"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    name = db.Column(db.String(30))
    hours = db.Column(db.Integer)
    desc = db.Column(db.String(140))
    item = db.Column(db.Boolean) #if item that can be counted as hour
    approved = db.Column(db.Boolean)

    def __init__(self, date, name, hours, desc, item, approved):
        self.date = date
        self.name = name
        self.hours = hours
        self.desc = desc
        self.item = item
        self.approved = approved

    def __repr__(self):
        return "<id{}>".format(self.id)


class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    tag = db.Column(db.String(10))
    title = db.Column(db.String(20))
    desc = db.Column(db.String(140))

    def __init__(self, date, tag, title, desc):
        self.date = date
        self.tag = tag
        self.title = title
        self.desc = desc

    def __repr__(self):
        return "<id{}>".format(self.id)
