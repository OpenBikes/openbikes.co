from flask import Flask, render_template, request, send_file, \
                  url_for, jsonify, g
from flask.ext.babel import Babel, gettext
from htmlmin import minify
from lib import routing
from lib import tools
import json

app = Flask(__name__)
babel = Babel(app)

cities = tools.read_json('static/cities.json')
names = tools.read_json('static/names.json')
stations = tools.read_json('static/stations.json')
centers = tools.read_json('static/centers.json')

#################
### Languages ###
#################

@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')

@babel.localeselector
def get_locale():
    return g.get('current_lang', 'en')

#################
### Main page ###
#################

@app.route('/')
def root():
    return minify(render_template('index.html', title=gettext('Maps - OpenBikes'),
                                  cities_file=cities, names_file=names,
                                  lang_code='en'))

@app.route('/<lang_code>')
def index():
    return minify(render_template('index.html', title=gettext('Maps - OpenBikes'),
                                  cities_file=cities, names_file=names))

############
### API ###
############

@app.route('/<lang_code>/api')
def api():
    return minify(render_template('api.html', title=gettext('API - OpenBikes'),
                                  cities_file=cities, stations_file=stations))

@app.route('/api/city/<city>', methods=['GET'])
def apicity_stations(city):
    ''' Return the latest geojson file of a city. '''
    stations = tools.read_json('static/geojson/{}.geojson'.format(city))
    return jsonify(stations)

@app.route('/api/stations', methods=['GET'])
def apistations():
    ''' Return the list of countries/cities/stations. '''
    stations = tools.read_json('static/stations.json')
    return jsonify(stations)

@app.route('/api/providers', methods=['GET'])
def apiproviders():
    ''' Return the list of providers/cities. '''
    providers = tools.read_json('static/providers.json')
    return jsonify(providers)

@app.route('/api/cities', methods=['GET'])
def apicities():
    ''' Return the list of countries/cities. '''
    cities = tools.read_json('static/cities.json')
    return jsonify(cities)

@app.route('/api/centers', methods=['GET'])
def apicenters():
    ''' Return the list of names. '''
    centers = tools.read_json('static/centers.json')
    return jsonify(centers)

@app.route('/api/names', methods=['GET'])
def apinames():
    ''' Return the list of names. '''
    names = tools.read_json('static/names.json')
    return jsonify(names)

@app.route('/api/routing/key=<key>&mode=<mode>&city=<city>&departure=<departure>&arrival=<arrival>&time=<time>&people=<people>', methods=['GET'])
def apirouting(mode, city, departure, arrival, time, people):
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
    if key == 'gershinowitz':
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

#################
### Products  ###
#################

@app.route('/<lang_code>/offer')
def offer():
    return minify(render_template('offer.html', title=gettext('Offer - OpenBikes')))

#############
### About ###
#############
    
@app.route('/<lang_code>/information')
def information():
    return minify(render_template('information.html', title=gettext('Information - OpenBikes')))

#################
### Live maps ###
#################

@app.route('/<lang_code>/<city>', methods=('GET', 'POST'))
def map(city):
    geojson=str(url_for('static',
                           filename='geojson/{}.geojson'.format(city)))
    return minify(render_template('map.html', city=city,
                           city_name=names[city],
                           center=centers[city],
                           geojson=str(url_for('static',
                           filename='geojson/{}.geojson'.format(city)))))

@app.route('/update')
def update():
    city = request.args.get('city', 0, type=str)
    update = open('static/updates/{}.txt'.format(city)).read()
    return jsonify({'timestamp': update})

@app.route('/route', methods=('GET', 'POST'))
def route():
    data = json.loads(request.data.decode())
    situation = {
        'city': data['city'],
        'departure': data['departure'],
        'arrival': data['arrival'],
        'people': int(data['people']),
        'time': data['time']
    }
    mode = data['mode']
    # Build the paths according to the travelling mode
    if mode == 'fullTrip':
        routes = routing.full_trip(situation)
    elif mode == 'takeBike':
        routes = routing.take_bike(situation)
    elif mode == 'dropBike':
        routes = routing.drop_bike(situation)
    return jsonify({'routes': routes})

#######################
### Handling errors ###
#######################

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message='404 not found'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', message='500 internal server error'), 500

#################
### Main loop ###
#################

if __name__ == '__main__':
    app.run(host='0.0.0.0')
