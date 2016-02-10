from flask import Blueprint, jsonify, render_template
from common import toolbox as tb
from common import files, folders


# Create a blueprint for the API views
apibp = Blueprint('apibp', __name__, url_prefix='/api')


@apibp.route('/city/<city>', methods=['GET'])
def api_city(city):
    ''' Return the latest geojson file of a city. '''
    geojson = tb.read_json('{0}/{1}.geojson'.format(folders.geojson, city))
    return render_template('json.html', result=geojson, title=city)


@apibp.route('/stations', methods=['GET'])
def api_stations():
    ''' Return the list of countries/cities/stations. '''
    stations = tb.read_json(files.stations)
    return render_template('json.html', result=stations, title='Stations')


@apibp.route('/providers', methods=['GET'])
def api_providers():
    ''' Return the list of providers/cities. '''
    providers = tb.read_json(files.providers)
    return render_template('json.html', result=providers, title='Providers')


@apibp.route('/cities', methods=['GET'])
def api_cities():
    ''' Return the list of countries/cities. '''
    cities = tb.read_json(files.cities)
    return render_template('json.html', result=cities, title='Cities')


@apibp.route('/centers', methods=['GET'])
def api_centers():
    ''' Return the list of names. '''
    centers = tb.read_json(files.centers)
    return render_template('json.html', result=centers, title='Centers')


@apibp.route('/names', methods=['GET'])
def api_names():
    ''' Return the list of names. '''
    names = tb.read_json(files.names)
    return render_template('json.html', result=names, title='Names')


@apibp.route('/predictions', methods=['GET'])
def api_predictions():
    ''' Return the list of predictions. '''
    predictions = tb.read_json(files.predictions)
    return render_template('json.html', result=predictions, title='Predictions')


@apibp.route('/updates', methods=['GET'])
def api_updates():
    ''' Return a dictionary containing the time of latest updates. '''
    updates = tb.read_json(files.updates)
    return render_template('json.html', result=updates, title='Updates')
