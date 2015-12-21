import argparse
import numpy as np
from common import toolbox as tb
from collecting.providers import *
from collecting import altitudes
from mongo.geo import insert

# Define the command line arguments
parser = argparse.ArgumentParser(description='Add a city to the system.')
parser.add_argument('provider')
parser.add_argument('city')
parser.add_argument('cityRealName')
parser.add_argument('country')
parser.add_argument('countryRealName')
parser.add_argument('predict')

# Parse the command line arguments
parameters = parser.parse_args()
provider = parameters.provider
city = parameters.city
cityRealName = parameters.cityRealName
country = parameters.country
countryRealName = parameters.countryRealName
predict = parameters.predict

# Load the information folder path
settings = tb.read_json('common/settings.json')
informationFolder = settings['folders']['information']

# Load the information files
stationsFile = tb.read_json('{}/stations.json'.format(informationFolder))
providersFile = tb.read_json('{}/providers.json'.format(informationFolder))
centersFile = tb.read_json('{}/centers.json'.format(informationFolder))
citiesFile = tb.read_json('{}/cities.json'.format(informationFolder))
namesFile = tb.read_json('{}/names.json'.format(informationFolder))
predictionsFile = tb.read_json('{}/predictions.json'.format(informationFolder))

# Get the current information for a city
stations = eval(provider).stations(city)
# Add the altitudes of every station
stations = altitudes.add(stations)
# Add the city and the stations to the database
insert.city(city, stations)
# Extract latitudes, longitudes and station names
latitudes = [station['lat'] for station in stations]
longitudes = [station['lon'] for station in stations]
names = [station['name'] for station in stations]
# City/Stations file
stationsFile[city] = names
# Provider/City file
if provider not in providersFile.keys():
    providersFile[provider] = []
    providersFile[provider].append(city)
else:
    if city not in providersFile[provider]:
        providersFile[provider].append(city)
# City/Center file
center = [np.mean(latitudes), np.mean(longitudes)]
centersFile[city] = center
# Country/City file
if country not in citiesFile:
    citiesFile[country] = []
    citiesFile[country].append(city)
else:
    if city not in citiesFile[country]:
        citiesFile[country].append(city)
# Name/RealName file
namesFile[city] = cityRealName
namesFile[country] = countryRealName
# Predictions file
predictionsFile[city] = predict
# Notification
print('{} has been added.'.format(city))

# Save the information files
tb.write_json(stationsFile, '{}/stations.json'.format(informationFolder))
tb.write_json(providersFile, '{}/providers.json'.format(informationFolder))
tb.write_json(centersFile, '{}/centers.json'.format(informationFolder))
tb.write_json(citiesFile, '{}/cities.json'.format(informationFolder))
tb.write_json(namesFile, '{}/names.json'.format(informationFolder))
tb.write_json(predictionsFile, '{}/predictions.json'.format(informationFolder))
