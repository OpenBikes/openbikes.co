import argparse
import os
from common import toolbox as tb
from common import folders, files
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

# Load the metadata files
stations_file = tb.read_json(files.stations)
providers_file = tb.read_json(files.providers)
centers_file = tb.read_json(files.centers)
cities_file = tb.read_json(files.cities)
names_file = tb.read_json(files.names)
predictions_file = tb.read_json(files.predictions)
updates_file = tb.read_json(files.updates)

# Geographical database
try:
    delete.city(city)
except:
    None
# geojson file
try:
    os.remove('{0}/{1}.geojson'.format(folders.geojson))
except:
    None
# City/Stations file
try:
    del stations_file[city]
except:
    None
# Provider/City file
try:
    providers_file[provider].remove(city)
except:
    None
try:
    if len(providers_file[provider]) == 0:
        del providers_file[provider]
except:
    None
try:
    if len(providers_file[provider]) == 0:
        del providers_file[provider]
except:
    None
# City/Center file
try:
    del centers_file[city]
except:
    None
# Country/City file
try:
    cities_file[country].remove(city)
except:
    None
try:
    if len(cities_file[country]) == 0:
        del cities_file[country]
except:
    None
# City/RealName file
try:
    del names_file[city]
except:
    None
try:
    if country not in cities_file:
        del names_file[country]
except:
    None
# Predictions file
try:
    del predictions_file[city]
except:
    None
# Updates file
try:
    del updates_file[city]
except:
    None
# Notification
print('{} has been removed.'.format(city))

# Save the metadata files
tb.write_json(stations_file, files.stations)
tb.write_json(providers_file, files.providers)
tb.write_json(centers_file, files.centers)
tb.write_json(cities_file, files.cities)
tb.write_json(names_file, files.names)
tb.write_json(predictions_file, files.predictions)
tb.write_json(predictions_file, files.updates)
