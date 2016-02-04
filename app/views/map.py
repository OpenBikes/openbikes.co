from flask import jsonify, render_template, url_for, request
from htmlmin import minify
import json
from common import toolbox as tb
from routing import trip
from app.forms import DropBike
from app.views import informationFolder
from app import app
import datetime


@app.route('/<lang_code>/<city>')
def map(city):
    names = tb.read_json('{}/names.json'.format(informationFolder))
    centers = tb.read_json('{}/centers.json'.format(informationFolder))
    predictions = tb.read_json('{}/predictions.json'.format(informationFolder))
    geojson = str(
        url_for('static', filename='geojson/{}.geojson'.format(city)))
    return minify(render_template('map.html', city=city, city_name=names[city],
                                  center=centers[city], geojson=geojson,
                                  predict=predictions[city],
                                  formDropBike=DropBike()))


@app.route('/update')
def update():
    city = request.args.get('city', 0, type=str)
    updates = tb.read_json('{}/updates.json'.format(informationFolder))
    update = updates[city]
    return jsonify({'timestamp': update})


@app.route('/route', methods=['POST'])
def route():
    situation = json.loads(request.data.decode())
    situation['people'] = int(situation['people'])
    situation['time'] = datetime.datetime.strptime(
        situation['time'], '%d-%m-%Y %H:%M')
    print(situation)
    mode = situation['mode']
    # Build the paths according to the travelling mode
    if 'fullTrip' in situation.keys():
        routes = trip.full_trip(situation)
    elif mode == 'takeBike':
        routes = trip.take_bike(situation)
    elif mode == 'dropBike':
        routes = trip.drop_bike(situation)
    return jsonify({'routes': routes})
