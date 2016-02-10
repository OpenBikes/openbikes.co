import datetime
from celery import Celery
from celery.decorators import periodic_task
from collecting.providers import *
from mongo.timeseries import insert, query
from learning import *
from common import toolbox as tb
from common import folders, files, settings

# Setup celery
celery = Celery('tasks')
celery.config_from_object('celery_config')


@celery.task
def update(provider, city, predict):
    ''' Update the data for a city. '''
    # Get the current formatted data for a city
    try:
        stations = eval(provider).stations(city)
    except:
        return
    # Update the database if the city can be predicted
    if predict == 'Yes':
        insert.city(city, stations)
    # Save the data for the map
    geojson = tb.json_to_geojson(stations)
    tb.write_json(geojson, '{0}/{1}.geojson'.format(folders.geojson, city))
    # Refresh the latest update time
    try:
        updates = tb.read_json(files.updates)
        updates[city] = datetime.datetime.now().isoformat()
        tb.write_json(updates, files.updates)
    except:
        return


@celery.task
def learn(city, station):
    ''' Train a predictor for a station and save it. '''
    # Get data from the past 30 days
    days = settings.learning['timespan']
    since = datetime.datetime.now() - datetime.timedelta(days=days)
    until = datetime.datetime.now()
    try:
        dataframe = query.station(city, station, since, until)
    except:
        return
    # Prepare the dataframe for learning
    dataframe = munging.prepare(dataframe)
    # Define the regression method
    regressor = eval(settings.learning['method'])
    # Apply the regressor that is chosen in the settings
    regressor.fit(dataframe, 'bikes', city, station)
    regressor.fit(dataframe, 'spaces', city, station)
