from django.db import models


# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=255)


class RichModel(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    date = models.DateField()
    age = models.PositiveSmallIntegerField()
    sex = models.BooleanField()
    gender = models.NullBooleanField()