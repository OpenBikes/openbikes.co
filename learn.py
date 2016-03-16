#!/usr/bin/python3
import datetime
from mongo.timeseries import query
from learning import *
from common import settings
from common import toolbox as tb
from common import files


def learn(station):
    ''' Train a predictor for a station and save it. '''
    # Get data from the past 30 days
    days = settings.learning['timespan']
    since = datetime.datetime.now() - datetime.timedelta(days=days)
    until = datetime.datetime.now()
    try:
        dataframe = query.station(city, station, since, until)
    except:
        return False, city
    # Prepare the dataframe for learning
    dataframe = munging.prepare(dataframe)
    # Define the regression method
    regressor = eval(settings.learning['method'])
    # Apply the regressor that is chosen in the settings
    regressor.fit(dataframe, 'bikes', city, station)
    regressor.fit(dataframe, 'spaces', city, station)
    return True, city


# Predictions file
predictions = tb.read_json(files.predictions)
# Stations file
stations = tb.read_json(files.stations)


if __name__ == '__main__':
    # Station regressors training
    for city, stations in stations.items():
        if predictions[city] == 'Yes':
            for station in stations:
                learn(station)
