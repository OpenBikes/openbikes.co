from pymongo import MongoClient, GEOSPHERE
import numpy as np

# Connect to the database
client = MongoClient()
db = client.OpenBikes_Geo

# 'p': position
# 'a': altitude


def add_city(city):
    ''' Initialize a collection for a city and create a 2D index. '''
    collection = db[city]
    collection.create_index([('p', GEOSPHERE)])


def delete_city(city):
    ''' Delete a city entry. '''
    collection = db[city]
    collection.drop()


def add_station(city, station, lat, lon, altitude):
    ''' Add a station with it's position to the database. '''
    collection = db[city]
    collection.save({'_id': station, 'p': [lon, lat], 'a': altitude})


def close_points(city, pos, number=100000, minDistance=0, maxDistance=np.inf):
    '''
    Input a latitude and a longitude in meters to return a
    list of close by points. A limit to the number of stations returned
    can be imposed. One can also set maximal and minimal ranges which
    are to be specified in meters and are circle radiuses. Be careful,
    MongoDB stores and returns the positions in with the [lon, lat]
    order, which isn't the most widespread convention.
    '''
    collection = db[city]
    lat = pos[0]
    lon = pos[1]
    query = {
        'p': {
            '$near': {
                '$geometry': {
                    'type': 'Point',
                    'coordinates': [lon, lat]
                },
                '$minDistance': minDistance,
                '$maxDistance': maxDistance
            }
        }
    }
    stations = collection.find(query).limit(number)
    return stations


def lat_lon(city, station):
    ''' Return the latitude and longitude of a station. '''
    collection = db[city]
    result = collection.find({'_id': station}, {'p': 1}).next()
    pos = result['p']
    lon = pos[0]
    lat = pos[1]
    return lat, lon
