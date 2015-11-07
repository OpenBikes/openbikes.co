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
parser.add_argument('predict')

# Parse the command line arguments
parameters = parser.parse_args()
option = parameters.option
provider = parameters.provider
city = parameters.city
cityRealName = parameters.cityRealName
country = parameters.country
countryRealName = parameters.countryRealName
predict = parameters.predict

# Load the files
stationsFile = tools.read_json('static/stations.json')
providersFile = tools.read_json('static/providers.json')
centersFile = tools.read_json('static/centers.json')
citiesFile = tools.read_json('static/cities.json')
namesFile = tools.read_json('static/names.json')
predictionsFile = tools.read_json('static/predictions.json')

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
    # Predictions file
    predictionsFile[city] = predict
    # Notification
    print('{} has been added.'.format(city))
elif option in ('delete', 'remove'):
    try:
        geo.delete_city(city)
    except:
        None
    # geoJson file
    try:
        os.remove('static/geojson/{}.geojson'.format(city))
    except:
        None
    # Update file
    try:
        os.remove('static/updates/{}.txt'.format(city))
    except:
        None
    # Geographical database
    try:
        geo.delete_city(city)
    except:
        None
    # City/Stations file
    try:
        del stationsFile[city]
    except:
        None
    # Provider/City file
    try:
        providersFile[provider].remove(city)
    except:
        None
    try:
        if len(providersFile[provider]) == 0:
            del providersFile[provider]
    except:
        None
    try:
        if len(providersFile[provider]) == 0:
            del providersFile[provider]
    except:
        None
    # City/Center file
    try:
        del centersFile[city]
    except:
        None
    # Country/City file
    try:
        citiesFile[country].remove(city)
    except:
        None
    try:
        if len(citiesFile[country]) == 0:
            del citiesFile[country]
    except:
        None
    # City/RealName file
    try:
        del namesFile[city]
    except:
        None
    try:
        if country not in citiesFile:
            del namesFile[country]
    except:
        None
    # Predictions file
    try:
        del predictionsFile[city]
    except:
        None
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
tools.dump_json(predictionsFile, 'static/predictions.json')
