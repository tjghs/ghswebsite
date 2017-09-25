from django.db import models


class Announcement(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
