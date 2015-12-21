import argparse
import os
from common import toolbox as tb
from mongo.geo import delete

# Define the command line arguments
parser = argparse.ArgumentParser(description='Remove a city from the system.')
parser.add_argument('provider')
parser.add_argument('city')
parser.add_argument('country')

# Parse the command line arguments
parameters = parser.parse_args()
provider = parameters.provider
city = parameters.city
country = parameters.country

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
updatesFile = tb.read_json('{}/updates.json'.format(informationFolder))

# Geographical database
try:
    delete.city(city)
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
# Updates file
try:
    del updatesFile[city]
except:
    None
# Notification
print('{} has been removed.'.format(city))

# Save the information files
tb.write_json(stationsFile, '{}/stations.json'.format(informationFolder))
tb.write_json(providersFile, '{}/providers.json'.format(informationFolder))
tb.write_json(centersFile, '{}/centers.json'.format(informationFolder))
tb.write_json(citiesFile, '{}/cities.json'.format(informationFolder))
tb.write_json(namesFile, '{}/names.json'.format(informationFolder))
tb.write_json(predictionsFile, '{}/predictions.json'.format(informationFolder))
tb.write_json(updatesFile, '{}/updates.json'.format(informationFolder))
