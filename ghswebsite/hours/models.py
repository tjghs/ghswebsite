from django.db import models

from user.models import User


class HourItem(models.Model):
    title = models.CharField(max_length=32, unique=True)
    hours = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return self.title


class HourRequest(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()
    description = models.CharField(max_length=50)
    item = models.ForeignKey(HourItem)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
