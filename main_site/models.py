from django.contrib.auth.models import User
from django.db import models

class QueryModel(models.Model):
    lattidute = models.FloatField()
    longitude = models.FloatField()
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.BooleanField()
