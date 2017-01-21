#!/usr/bin/python3
from app import db
from sqlalchemy.dialects.postgresql import JSON


class Hours(db.Model):
    __tablename__ = "hours"

    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, primary_key=True)
    desc = db.Column(db.String(), primary_key=True)
    hours = db.Column(db.Integer)
    date = db.Column(db.Date, primary_key=True)
    item = db.Column(db.Boolean, primary_key=True) #if item that can be counted as hour

    def __init__(self, admin, desc, hours, date, item):
        self.desc = desc
        self.admin = admin
        self.hours = hours
        self.date = date
        self.item = item

    def __repr__(self):
        return "<id{}>".format(self.id)


class Announcements(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), primary_key=True)
    tag = db.Column(db.String(), primary_key=True)
    desc = db.Column(db.String())
    date = db.Column(db.Date, primary_key=True)

    def __init__(self, title, tag, desc, date):
        self.title = title
        self.tag = tag
        self.desc = desc
        self.date = date

    def __repr__(self):
        return "<id{}>".format(self.id)
