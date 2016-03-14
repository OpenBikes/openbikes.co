#!/usr/bin/python3
import datetime
from mongo.timeseries import query
from learning import *
from common import settings

# Setup celery
from celery import Celery
celery = Celery('openbikes')
celery.config_from_object('learning.celeryconfig')


@celery.task
def learn(city, stations):
    ''' Train a predictor for a station and save it. '''
    # Get data from the past 30 days
    days = settings.learning['timespan']
    since = datetime.datetime.now() - datetime.timedelta(days=days)
    until = datetime.datetime.now()
    for station in stations:
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
