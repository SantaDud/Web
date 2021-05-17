from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, related_name= "Departures", on_delete = models.CASCADE)
    destination = models.ForeignKey(Airport, related_name= 'Arrivals', on_delete = models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} Duration: {self.duration} minutes"

class Passenger(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank= True, related_name='Passenger')

    def __str__(self):
        return f'{self.fname} {self.lname}'