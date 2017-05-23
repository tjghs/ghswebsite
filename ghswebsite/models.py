from ghswebsite.app import db
# from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(20))
    last = db.Column(db.String(20))
    username = db.Column(db.String(12))
    hours = db.Column(db.Integer)

    def __init__(self, first, last, username, hours):
        self.first = first
        self.last = last
        self.username = username
        self.hours = hours

    def __repr__(self):
        return "<id{}>".format(self.id)


class Hour(db.Model):
    __tablename__ = "hours"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    user = db.Column(db.String(12))
    hours = db.Column(db.Integer)
    desc = db.Column(db.String(140))
    item = db.Column(db.Boolean) # if item that can be counted as hour
    # approved = db.Column(db.Boolean)

    def __init__(self, date, user, hours, desc, item):
        self.date = date
        self.user = user
        self.hours = hours
        self.desc = desc
        self.item = item
        # self.approved = approved

    def __repr__(self):
        return "<id{}>".format(self.id)


class Announcement(db.Model):
    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    tag = db.Column(db.String(10))
    title = db.Column(db.String(100))
    desc = db.Column(db.String(500))

    def __init__(self, date, tag, title, desc):
        self.date = date
        self.tag = tag
        self.title = title
        self.desc = desc

    def __repr__(self):
        return "<id{}>".format(self.id)
