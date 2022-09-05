from django.db import models
import requests, json

# Create your models here.
# class flightDataManager(models.Manager):
#     def add_flight(self, time, callsign):
#         flight = self.create(time = time, callsign = callsign)
#         return flight
class flightData(models.Model):
    time = models.CharField(max_length=100)
    callsign = models.CharField(max_length=100)
    # objects = flightDataManager()
API = "https://opensky-network.org/api/states/all"
result = requests.get(API)
data = result.json()
ftime = data.get("time")
callsign = data.get("states")[0][1]
print(ftime, callsign)
flight = flightData.objects.create(time = ftime, callsign = callsign)
flight.save()