#!/usr/bin/python3
import sys
import argparse
import numpy as np
from common import toolbox as tb
from common import files
from collecting.providers import *
from collecting import altitudes
from mongo.geo import insert

# Define the command line arguments
parser = argparse.ArgumentParser(description='Add a city to the system.')
# Data provider
parser.add_argument('provider')
# City OpenBikes name
parser.add_argument('city')
# City local name
parser.add_argument('city_real_name')
# OpenWeatherMap name
parser.add_argument('city_owm_name')
# Country OpenBikes name
parser.add_argument('country')
# Country local name
parser.add_argument('countryRealName')
# Is prediction activated
parser.add_argument('predict')

# Parse the command line arguments
parameters = parser.parse_args()
provider = parameters.provider
city = parameters.city
city_real_name = parameters.city_real_name
city_owm_name = parameters.city_owm_name
country = parameters.country
country_real_name = parameters.countryRealName
predict = parameters.predict

# Load the metadata files
stations_file = tb.read_json(files.stations)
providers_file = tb.read_json(files.providers)
centers_file = tb.read_json(files.centers)
cities_file = tb.read_json(files.cities)
names_file = tb.read_json(files.names)
predictions_file = tb.read_json(files.predictions)
owm_file = tb.read_json(files.owm)

# Get the current information for a city
try:
    stations = eval(provider).stations(city)
    # Add the altitudes of every station
    stations = altitudes.add(stations)
    # Add the city and the stations to the geographical database
    insert.city(city, stations)
except:
    print("Problem adding {}.".format(city))
    sys.exit()
# Extract latitudes, longitudes and station names
latitudes = [station['lat'] for station in stations]
longitudes = [station['lon'] for station in stations]
names = [station['name'] for station in stations]
# City/Stations file
stations_file[city] = names
# Provider/City file
if provider not in providers_file.keys():
    providers_file[provider] = []
    providers_file[provider].append(city)
else:
    if city not in providers_file[provider]:
        providers_file[provider].append(city)
# City/Center file
center = [np.mean(latitudes), np.mean(longitudes)]
centers_file[city] = center
# Country/City file
if country not in cities_file:
    cities_file[country] = []
    cities_file[country].append(city)
else:
    if city not in cities_file[country]:
        cities_file[country].append(city)
# Name/RealName file
names_file[city] = city_real_name
names_file[country] = country_real_name
# Predictions file
predictions_file[city] = predict
# OpenWeatherMap file
owm_file[city] = city_owm_name
# Notification
print('{} has been added.'.format(city))

# Save the metadata files
tb.write_json(stations_file, files.stations)
tb.write_json(providers_file, files.providers)
tb.write_json(centers_file, files.centers)
tb.write_json(cities_file, files.cities)
tb.write_json(names_file, files.names)
tb.write_json(predictions_file, files.predictions)
tb.write_json(owm_file, files.owm)
