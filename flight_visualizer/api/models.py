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
states = data.get("states")
print(len(states))
for i, flight in enumerate(states):
    flightdata = flightData.objects.create(time = ftime, callsign = flight[1])
    print(flightdata)
    flightdata.save()