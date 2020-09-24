from django.db import models


class Vehicle(models.Model):
  #id field added automatically
    plate = models.CharField(max_length=50)



class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

