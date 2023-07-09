from django.db import models

# Create your models here.
class flighinfo(models.Model):
    flightno=models.IntegerField()
    fromm=models.CharField(max_length=100)
    to=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    capacity=models.IntegerField()

