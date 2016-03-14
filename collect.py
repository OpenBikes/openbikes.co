#!/usr/bin/python3
from collecting.providers import *
from mongo.timeseries import insert
from common import toolbox as tb
from common import folders

# Setup celery
from celery import Celery
celery = Celery('openbikes')
celery.config_from_object('collecting.celeryconfig')


@celery.task
def collect(provider, city, predict):
    ''' Update the data for a city. '''
    # Get the current formatted data for a city
    try:
        stations = eval(provider).stations(city)
    except:
        return False, city
    # Update the database if the city can be predicted
    if predict == 'Yes':
        insert.city(city, stations)
    # Save the data for the map
    geojson = tb.json_to_geojson(stations)
    tb.write_json(geojson, '{0}/{1}.geojson'.format(folders.geojson, city))
    return True, city
