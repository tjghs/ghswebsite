#!ghswebsite/bin/python3
import sys
import datetime
from app import db
from models import Announcement


def add(tag, title, desc):
    newAnnouncement = Announcement(datetime.datetime.now(), tag, title, desc)
    db.session.add(newAnnouncement)
    db.session.commit()
    print("New announcement " + title + " created.")


def delete(title):
    Announcement.query.filter_by(title=title).delete(synchronize_session=False)
    db.session.commit()

if len(sys.argv) >= 3:
    if sys.argv[1] == "add":
        add(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "del":
        delete(sys.argv[2])
    else:
        print(
            "usage: add or delete announcement database entries <tag> <title> <description>")
        exit(1)
else:
    print("usage: add or delete announcement database entries <tag> <title> <description>")
    exit(1)
