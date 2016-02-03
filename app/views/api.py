from flask import Blueprint, jsonify
from common import toolbox as tb
from app.views import geojsonFolder, informationFolder


# Create a blueprint for the API views
apibp = Blueprint('apibp', __name__, url_prefix='/api')


@apibp.route('/city/<city>', methods=['GET'])
def api_city_stations(city):
    ''' Return the latest geojson file of a city. '''
    stations = tb.read_json('{0}/{1}.geojson'.format(geojsonFolder, city))
    return jsonify(stations)


@apibp.route('/stations', methods=['GET'])
def api_stations():
    ''' Return the list of countries/cities/stations. '''
    stations = tb.read_json('{}/stations.json'.format(informationFolder))
    return jsonify(stations)


@apibp.route('/providers', methods=['GET'])
def api_providers():
    ''' Return the list of providers/cities. '''
    providers = tb.read_json('{}/providers.json'.format(informationFolder))
    return jsonify(providers)


@apibp.route('/cities', methods=['GET'])
def api_cities():
    ''' Return the list of countries/cities. '''
    cities = tb.read_json('{}/cities.json'.format(informationFolder))
    return jsonify(cities)


@apibp.route('/centers', methods=['GET'])
def api_centers():
    ''' Return the list of names. '''
    centers = tb.read_json('{}/centers.json'.format(informationFolder))
    return jsonify(centers)


@apibp.route('/names', methods=['GET'])
def api_names():
    ''' Return the list of names. '''
    names = tb.read_json('{}/names.json'.format(informationFolder))
    return jsonify(names)


@apibp.route('/predictions', methods=['GET'])
def api_predictions():
    ''' Return the list of predictions. '''
    predictions = tb.read_json('{}/predictions.json'.format(informationFolder))
    return jsonify(predictions)


@apibp.route('/updates', methods=['GET'])
def api_updates():
    ''' Return the list of update times. '''
    updates = tb.read_json('{}/updates.json'.format(informationFolder))
    return jsonify(updates)


@apibp.route('/routing/key=<key>&mode=<mode>&city=<city>&' +
             'departure=<departure>&arrival=<arrival>&time=<time>' +
             '&people=<people>', methods=['GET'])
def api_routing(mode, city, departure, arrival, time, people):
    '''
    Return a list of routes in polyline format.
    String adresses are not supported because they
    won't be needed for the mobile apps. Indeed the
    departure will be the same as the arrival because
    the mobile apps do not include full trips.

    Example URL:

        /routing/mode=takeBike&city=Toulouse&
        departure=[43.5639677,1.4655774]&
        arrival=[43.6044328,1.443463]&
        time=[1442935490355]&people=1

    Don't forget to remove all the spaces.
    '''
    if key == tb.read_json('config/keys.json')['api']:
        situation = {
            'city': city,
            'departure': eval(departure),
            'arrival': eval(arrival),
            'time': eval(time),
            'people': int(people)
        }
        if mode == 'fullTrip':
            routes = routing.full_trip(situation)
        elif mode == 'takeBike':
            routes = routing.take_bike(situation)
        elif mode == 'dropBike':
            routes = routing.drop_bike(situation)
        return jsonify({'routes': routes})
    else:
        return jsonify({'error': 'Wrong API key.'})
