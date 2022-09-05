from sys import maxsize
from django.db import models
import requests
import json 

class flightData(models.Model):
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    callsign = models.CharField(max_length=20)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    carbon_emissions = models.IntegerField()

path = "https://opensky-network.org/api/states/all"

data = requests.get(path)
data = data.json()


departure_time = data.get("time")
callsign = data.get("states")[0][1]

for i in range(len(data.get("states"))):
    flight = flightData.objects.create(time = departure_time, callsign = data[i][1])
    flight.save()






