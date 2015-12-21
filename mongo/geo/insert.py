from pymongo import GEOSPHERE
from mongo.geo import db


# 'p': position
# 'a': altitude


def city(city, stations):
    ''' Initialize a collection for a city and create a 2D index. '''
    collection = db[city]
    collection.create_index([('p', GEOSPHERE)])
    for station in stations:
        insert_station(collection, station)


def insert_station(collection, station):
    ''' Add a station with it's position to the database. '''
    name = station['name']
    lon = station['lon']
    lat = station['lat']
    alt = station['alt']
    collection.save({'_id': name, 'p': [lon, lat], 'a': alt})
