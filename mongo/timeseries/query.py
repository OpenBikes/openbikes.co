from datetime import datetime
import pandas as pd
from mongo.timeseries import db


# 'u': updates
# 'i': information
# 'm': update time
# 'b': available bikes
# 's': available stands
# 't': temperature
# 'h': humidity
# 'w': speed
# 'c': cloudiness


def station(city, station, threshold):
    '''
    Returns a dictionary of dataframes containing all the updates of a given
    period or day for a station, up to a given threshold. The threshold is a
    Python datetime object.
    '''
    # Connect to the appropriate collection of the database
    collection = db[city]
    # Query the station's updates
    pattern = threshold.isoformat()
    cursor = collection.find({'_id': {'$gte': pattern}, 'u.n': station},
                             {'u': {'$elemMatch': {'n': station}}})
    # We will modify the index so as to take into account the date
    fmt = '%Y-%m-%d/%H:%M:%S'
    # Create the dataframe with the first date
    dataframe = pd.DataFrame(cursor[0]['u'][0]['i']).set_index('m')
    dataframe.index = dataframe.index.map(
        lambda i: datetime.strptime('/'.join((cursor[0]['_id'], i)), fmt))
    # Add the updates from every other date
    for date in cursor[1:]:
        try:
            df = pd.DataFrame(date['u'][0]['i']).set_index('m')
            df.index = df.index.map(
                lambda i: datetime.strptime('/'.join((date['_id'], i)), fmt))
            dataframe = pd.concat((dataframe, df))
        except:
            pass
    return dataframe


def city(city, year='\d{4}', month='\d{1,2}', day='\d{1,2}'):
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
        datesDfs[date['_id']] = {
            update['n']: pd.DataFrame(update['i']).set_index('m')
            for update in date['u']
            if len(update['i']) > 0
        }
    # Now we can merge the dataframes for every station
    stationsDfs = {}
    for date, stations in datesDfs.items():
        for station, df in stations.items():
            # Add the date to the time for a unique index
            df.index = df.index.map(
                lambda i: datetime.strptime('/'.join((date, i)), fmt))
            # Concatenate the daily dataframes into one for the month
            if station in stationsDfs.keys():
                stationsDfs[station] = pd.concat((stationsDfs[station], df))
            else:
                stationsDfs[station] = df
    return stationsDfs
