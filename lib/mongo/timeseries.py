from pymongo import MongoClient
from datetime import datetime
import pandas as pd
from lib import tools
from lib.mongo import geo

# Connect to the database
client = MongoClient()
db = client.OpenBikes


# 'u': updates                
# 'i': information
# 'm': update time
# 'b': available bikes
# 's': available stands
# 't': temperature
# 'h': humidity
# 'w': speed
# 'c': cloudiness


def delete_city(city):
    ''' Destroy a collection. '''
    db.drop_collection(city)


# Insertions


def update_station(station, collection):
    ''' Add the latest update of a station. '''
    name = station['name']
    timestamp = datetime.strptime(station['update'], '%Y-%m-%dT%H:%M:%S')
    time = timestamp.time().isoformat()
    date = timestamp.date().isoformat()
    # Check the dates has already been inserted
    if collection.find({'_id': date}, {'_id': 1}).limit(1).count() == 0:
        collection.save({
            '_id': date,
            'u': []
        })
    # Add the station entry if it doesn't exist and there is data
    if collection.find({'_id': date, 'u.n': name},
                       {'_id': 1}).limit(1).count() == 0:
        collection.update({'_id': date, 'u.n': {'$nin': [name]}}, {
            '$push': {
                'u': {
                    'n': name,
                    'i': []
                }
            }
        })
    collection.update({'_id': date, 'u.n': name}, {
        '$addToSet': {
            'u.$.i': {
                'm': time,
                'b': station['bikes'],
                's': station['stands']
            }
        }
    })


def update_city(stations, city):
    ''' Add the latest update from every station in a city. '''
    # Connect to the appropriate collection of the database
    collection = db[city]
    # Update every station
    for station in stations:
        update_station(station, collection)

# Queries


def query_station(city, station, year='\d{4}', month='\d{1,2}', day='\d{1,2}'):
    '''
    Returns a dictionary of dataframes containing all the updates
    of a given period or day for a station. You can use regular
    expressions for specific queries.
    '''
    # Connect to the appropriate collection of the database
    collection = db[city]
    # Query the station's updates
    pattern = '-'.join((year, month, day))
    cursor = collection.find({'_id': {'$regex': pattern}, 'u.n': station},
                             {'u': {'$elemMatch': {'n': station}}})
    # We will modify the index so as to take into account the date
    fmt = '%Y-%m-%d/%H:%M:%S'
    # Create the dataframe with the first date
    dataframe = tools.dict_to_dataframe(cursor[0]['u'][0]['i']).set_index('m')
    dataframe.index = dataframe.index.map(lambda i: datetime.strptime('/'.join((cursor[0]['_id'], i)), fmt))
    # Add the updates from every other date
    for date in cursor[1:]:
        try:
            df = tools.dict_to_dataframe(date['u'][0]['i']).set_index('m')
            df.index = df.index.map(lambda i: datetime.strptime('/'.join((date['_id'], i)), fmt))
            dataframe = pd.concat((dataframe, df))
        except:
            pass
    return dataframe


def query_city(city, year='\d{4}', month='\d{1,2}', day='\d{1,2}',
               merge=False):
    '''
    Returns a dictionary of dataframes containing all the updates
    of a given period or day for a city. You can use regular
    expressions for specific queries.
    '''
    # Connect to the appropriate collection of the database
    collection = db[city]
    # Query the city's updates
    pattern = '-'.join((year, month, day))
    cursor = collection.find({'_id': {'$regex': pattern}})
    # We will modify the index so as to take into account the date
    fmt = '%Y-%m-%d/%H:%M:%S'
    # Create a dictionary that will contain the dataframes
    datesDfs = {}
    # Iterate over every date
    for date in cursor:
        # Convert all the updates to a dictionary of dataframes indexed on time
        datesDfs[date['_id']] = {update['n']:
                                 tools.dict_to_dataframe(update['i']).set_index('m')
                                 for update in date['u'] if len(update['i']) > 0}
    # Now we can merge the dataframes for every station
    stationsDfs = {}
    for date, stations in datesDfs.items():
        for station, df in stations.items():
            # Add the date to the time for a unique index
            df.index = df.index.map(lambda i: datetime.strptime('/'.join((date, i)), fmt))
            # Concatenate the daily dataframes into one for the month
            if station in stationsDfs.keys():
                stationsDfs[station] = pd.concat((stationsDfs[station], df))
            else:
                stationsDfs[station] = df
    if merge is True:
        # Add the latitudes and longitudes to the dataframe
        blacklist = []
        for station in stationsDfs.keys():
            try:
                lat, lon = geo.lat_lon(city, station)
                stationsDfs[station]['lat'] = lat
                stationsDfs[station]['lon'] = lon
            except:
                blacklist.append(station)
        for station in blacklist:
            del stationsDfs[station]
        return pd.concat((df for df in stationsDfs.values()))
    return stationsDfs
