from operator import mod
from sys import maxsize
from django.db import models
import requests
import json 

class FlightData(models.Model):
    time = models.CharField(max_length=20, default=0)
    callsign = models.CharField(max_length=20, default=0)
    lat = models.CharField(max_length=20, default=0)
    long = models.CharField(max_length=20, default=0)
    velocity = models.CharField(max_length=20, default=0)
    true_track = models.CharField(max_length=20, default=0)
    carbon = models.CharField(max_length=20, default=0)

path = "https://opensky-network.org/api/states/all"

data1 = requests.get(path)
data = data1.json()
states = data.get("states")
departure_time = data.get("time")

# flight_data = FlightData.objects.create(time = departure_time, callsign = states[0][1], 
# lat = states[0][6], long = states[0][5], velocity = states[0][9], true_track = states[0][10], carbon = 0)
# flight_data.save()



# for i, flight in enumerate(states):
#     if i == 1000:
#         break
#     flightdata = FlightData.objects.create(time = departure_time, callsign = flight[1])
#     flightdata.save()






