from lib.providers import wrapper
from lib import geography
from lib.mongo import geo
from lib import tools
import argparse
import numpy as np
import os

# Define the command line arguments
parser = argparse.ArgumentParser(description='Add or remove a city.')
parser.add_argument('option')
parser.add_argument('provider')
parser.add_argument('city')
parser.add_argument('cityRealName')
parser.add_argument('country')
parser.add_argument('countryRealName')

# Parse the command line arguments
parameters = parser.parse_args()
option = parameters.option
provider = parameters.provider
city = parameters.city
cityRealName = parameters.cityRealName
country = parameters.country
countryRealName = parameters.countryRealName

# Load the files
stationsFile = tools.read_json('static/stations.json')
providersFile = tools.read_json('static/providers.json')
centersFile = tools.read_json('static/centers.json')
citiesFile = tools.read_json('static/cities.json')
namesFile = tools.read_json('static/names.json')

if option in ('add', 'insert'):
    geo.add_city(city)
    # Get the current information for a city
    stations = wrapper.collect(provider, city)
    # Add the altitudes of every station
    stations = geography.add_altitudes(stations)
    # Extract latitudes, longitudes and station names
    latitudes = []
    longitudes = []
    names = []
    for station in stations:
        latitudes.append(station['lat'])
        longitudes.append(station['lon'])
        names.append(station['name'])
        geo.add_station(city, station['name'],
        station['lat'], station['lon'], station['alt'])
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
    # Notification
    print ('{} has been added.'.format(city))
elif option in ('delete', 'remove'):
    geo.delete_city(city)
    # geoJson file
    os.remove('static/geojson/{}.geojson'.format(city))
    # Update file
    os.remove('static/updates/{}.txt'.format(city))
    # Geographical database
    geo.delete_city(city)
    # City/Stations file
    del stationsFile[city]
    # Provider/City file
    providersFile[provider].remove(city)
    if provider not in providersFile.keys():
        del providersFile[provider]
    # City/Center file
    del centersFile[city]
    # Country/City file
    citiesFile[country].remove(city)
    if len(citiesFile[country]) == 0:
        del citiesFile[country]
    # City/RealName file
    del namesFile[city]
    # Notification
    print('{} has been removed.'.format(city))
else:
    print('Invalid management argument.')

# Save the files
tools.dump_json(stationsFile, 'static/stations.json')
tools.dump_json(providersFile, 'static/providers.json')
tools.dump_json(centersFile, 'static/centers.json')
tools.dump_json(citiesFile, 'static/cities.json')
tools.dump_json(namesFile, 'static/names.json')