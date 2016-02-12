from flask import jsonify, render_template, url_for, request
from htmlmin import minify
import json
from datetime import datetime
from common import toolbox as tb
from common import files
from routing import handling
from app.forms import DropBike, PickBike, FullTrip
from app import app


@app.route('/city/<city>')
def map(city):
    names = tb.read_json(files.names)
    centers = tb.read_json(files.centers)
    predictions = tb.read_json(files.predictions)
    geojson = str(url_for('static', filename='geojson/{}.geojson'.format(city)))
    return minify(render_template('map.html', city=city, city_name=names[city],
                                  title='{} - OpenBikes'.format(city),
                                  center=centers[city], geojson=geojson,
                                  predict=predictions[city],
                                  formDropBike=DropBike(),
                                  formPickBike=PickBike(),
                                  formFullTrip=FullTrip()))


@app.route('/update')
def update():
    ''' Refresh the map with the latest geoJSON file. '''
    city = request.args.get('city', 0, type=str)
    updates = tb.read_json(files.updates)
    update = updates[city]
    return jsonify({'timestamp': update})


@app.route('/route', methods=['POST'])
def route():
    ''' Handle the trips chosen by the users. '''
    situation = json.loads(request.data.decode())
    situation['people'] = int(situation['people'])
    situation['time'] = datetime.strptime(situation['time'], '%d-%m-%Y %H:%M').timestamp()
    mode = situation['mode']
    # Build the paths according to the travelling mode
    if mode == 'fullTrip':
        routes = handling.full_trip(situation)
    elif mode == 'takeBike':
        routes = handling.take_bike(situation)
    elif mode == 'dropBike':
        routes = handling.drop_bike(situation)
    return jsonify({'routes': routes})
