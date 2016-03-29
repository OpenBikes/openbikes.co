from flask import Blueprint, jsonify
import os
import glob
from datetime import datetime
from common import toolbox as tb
from common import files, folders, settings
from learning import *


# Create a blueprint for the API views
apibp = Blueprint('apibp', __name__, url_prefix='/api')


@apibp.route('/geojson/<city>', methods=['GET'])
def api_city(city):
    ''' Return the latest geojson file of a city. '''
    geojson = tb.read_json('{0}/{1}.geojson'.format(folders.geojson, city))
    # City doesn't exist
    if geojson is False:
        return jsonify({
            'status': 'failure',
            'message': 'Unrecognized city name.'
        })
    # Geojson file of a city
    else:
        geojson['status'] = 'success'
        return jsonify(geojson)


@apibp.route('/stations', defaults = {'city': None}, methods=['GET'])
@apibp.route('/stations/<city>', methods=['GET'])
def api_stations(city):
    ''' Return the list of stations. '''
    stations = tb.read_json(files.stations)
    # All stations
    if city is None:
        return jsonify({
            'status': 'success',
            'data': [
                {
                    'city': name,
                    'stations': stations
                }
                for name, stations in stations.items()
            ]
        })
    # City doesn't exist
    elif city not in stations.keys():
        return jsonify({
            'status': 'failure',
            'message': 'Unrecognized city name.'
        })
    # Stations of a city
    else:
        return jsonify({
            'status': 'success',
            'city': city,
            'stations': stations[city]
        })


@apibp.route('/providers', defaults = {'provider': None}, methods=['GET'])
@apibp.route('/providers/<provider>', methods=['GET'])
def api_providers(provider):
    ''' Return the list of providers and the associated cities. '''
    providers = tb.read_json(files.providers)
    # All providers
    if provider is None:
        return jsonify({
            'status': 'success',
            'data': [
                {
                    'provider': name,
                    'cities': cities
                }
                for name, cities in providers.items()
            ]
        })
    # Provider doesn't exist
    elif provider not in providers.keys():
        return jsonify({
            'status': 'failure',
            'message': 'Unrecognized provider name.'
        })
    # Cities of a provider
    else:
        return jsonify({
            'status': 'success',
            'provider': provider,
            'cities': providers[provider]
        })


@apibp.route('/countries', defaults = {'country': None}, methods=['GET'])
@apibp.route('/countries/<country>', methods=['GET'])
def api_cities(country):
    ''' Return the list of countries and the associated cities. '''
    cities = tb.read_json(files.cities)
    # All countries
    if country is None:
        return jsonify({
            'status': 'success',
            'data': [
                {
                    'country': name,
                    'cities': cities
                }
                for name, cities in cities.items()
            ]
        })
    # Country doesn't exist
    elif country not in cities.keys():
        return jsonify({
            'status': 'failure',
            'message': 'Unrecognized country name.'
        })
    # Cities of a country
    else:
        return jsonify({
            'status': 'success',
            'country': country,
            'cities': cities[country]
        })


@apibp.route('/centers', defaults = {'city': None}, methods=['GET'])
@apibp.route('/centers/<city>', methods=['GET'])
def api_centers(city):
    ''' Return the center of each city. '''
    centers = tb.read_json(files.centers)
    # All centers
    if city is None:
        return jsonify({
            'status': 'success',
            'data': [
                {
                    'status': 'success',
                    'city': name,
                    'position': position
                }
                for name, position in centers.items()
            ]
        })
    # City doesn't exist
    elif city not in centers.keys():
        return jsonify({
            'status': 'failure',
            'message': 'Unrecognized city name.'
        })
    # Center of a city
    else:
        return jsonify({
            'status': 'success',
            'city': city,
            'center': centers[city]
        })


@apibp.route('/updates', defaults = {'city': None}, methods=['GET'])
@apibp.route('/updates/<city>', methods=['GET'])
def api_updates(city):
    ''' Return the list of latest updates for each city. '''
    geojson_files = glob.glob('{}/*.geojson'.format(folders.geojson))
    updates = {geojson.split('/')[-1].split('.')[0]: os.path.getmtime(geojson)
               for geojson in geojson_files}
    # All updates
    if city is None:
        return jsonify({
            'status': 'success',
            'data': [
                {
                    'status': 'success',
                    'city': name,
                    'update': update
                }
                for name, update in updates.items()
            ]
        })
    # City doesn't exist
    elif city not in updates.keys():
        return jsonify({
            'status': 'failure',
            'message': 'Unrecognized city name.'
        })
    # Update for a city
    else:
        return jsonify({
            'status': 'success',
            'city': city,
            'update': updates[city]
        })


@apibp.route('/prediction/<city>/<station>/<timestamp>', methods=['GET'])
def api_prediction(city, station, timestamp):
    ''' Return a prediction for a station at a given time. '''
    timestamp = float(timestamp)
    stations = tb.read_json(files.stations)
    predictions = tb.read_json(files.predictions)
    # City doesn't exist
    if city not in stations.keys():
         return jsonify({
             'status': 'failure',
             'message': 'Unrecognized city name.'
         })
    # Station doesn't exist
    elif station not in stations[city]:
        return jsonify({
            'status': 'failure',
            'message': 'Unrecognized station name.'
        })
    # Timestamp is in the past
    elif timestamp < datetime.now().timestamp():
        return jsonify({
            'status': 'failure',
            'message': 'Predictions in the past are not possible.'
        })
    # Predictions not enabled
    elif predictions[city] == 'No':
        return jsonify({
            'status': 'failure',
            'message': 'Predictions are not enabled for this city.'
        })
    # Prediction for a station
    else:
        moment = datetime.fromtimestamp(timestamp)
        features = [moment.hour, moment.minute, moment.weekday()]
        method = eval(settings.learning['method'])
        bikes = method.predict(features, 'bikes', city, station)
        spaces = method.predict(features, 'spaces', city, station)
        bias = settings.learning['bias']
        return jsonify({
            'status': 'success',
            'city': city,
            'station': station,
            'timestamp': timestamp,
            'bikes': {
                'quantity': bikes,
                'std': bias
            },
            'stands': {
                'quantity': spaces,
                'std': bias
            }
        })
