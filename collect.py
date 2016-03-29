#!/usr/bin/python3
from collecting.providers import *
from collecting import openweathermap as owm
from mongo.timeseries import insert as insert_bikes
from mongo.weather import insert as insert_weather
from common import toolbox as tb
from common import folders

# Setup celery
from celery import Celery
celery = Celery('openbikes')
celery.config_from_object('collecting.celeryconfig')


@celery.task
def bikes(provider, city, predict):
    ''' Update the bikes data for a city. '''
    # Get the current formatted data for a city
    try:
        stations = eval(provider).stations(city)
    except:
        return False, city
    # Update the database if the city can be predicted
    if predict == 'Yes':
        insert_bikes.city(city, stations)
    # Save the data for the map
    geojson = tb.json_to_geojson(stations)
    tb.write_json(geojson, '{0}/{1}.geojson'.format(folders.geojson, city))
    return True, city


@celery.task
def weather(city, city_id):
    '''
    Update the weather data for a city. The city_id parameter is the name of the
    city in the OpenWeatherMap database.
    '''
    # Get the current formatted data for a city
    try:
        weather = owm.weather(city_id)
    except:
        return False, city
    # Save the data for the map
    insert_weather.city(city, weather)
    return True, city
