from django.db import models

# Create your models here.
class User(models.Model):
    #__tablename__ = "users"

    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    username = models.CharField(max_length=12)


class Hour(db.Model):
    #__tablename__ = "hours"

    date = models.dateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours = models.integerField()
    desc = models.CharField(max_length=50)
    item = models.BooleanField(default=False)  # if item that can be counted as hour
    # approved = models.BooleanField(default=False)


class Announcement(db.Model):
    #__tablename__ = "announcements"

    date = models.dateField()
    tag = db.Column(db.String(10))
    title = db.Column(db.String(100))
    desc = models.CharField(max_length=500)
