from lib import geography
from lib import tools
from lib.mongo import geo
from lib.learning import wrapper
from copy import deepcopy
import json


def take_bike(situation):
    path = generate_path(situation, 'bikes', 'walking', 'pedestrian')
    route = generate_route(path)
    return [route]


def drop_bike(situation):
    path = generate_path(situation, 'spaces', 'cycling', 'bicycle')
    route = generate_route(path)
    return [route]


def full_trip(situation):
    ''' We can use the previous functions. '''
    # Find the route from the departure to the departure station
    firstSituation = deepcopy(situation)
    firstSituation['arrival'] = firstSituation['departure']
    firstPath = generate_path(firstSituation, 'bikes', 'walking', 'pedestrian')
    # Find the route from the arrival station to the arrival
    secondSituation = deepcopy(situation)
    secondSituation['departure'] = secondSituation['arrival']
    secondPath = generate_path(secondSituation, 'spaces', 'walking',
                               'pedestrian', stationFirst=True)
    # Find the route between both stations
    firstStation = firstPath['points'][1]
    secondStation = secondPath['points'][0]
    A = [firstStation['lat'], firstStation['lon']]
    B = [secondStation['lat'], secondStation['lon']]
    intermediatePath = reshape('bicycle', A, B)
    # Generate the routes
    routes = [generate_route(firstPath),
              generate_route(intermediatePath),
              generate_route(secondPath)]
    return routes


def generate_path(situation, target, distance, mode, stationFirst=False,
                  nbCandidates=5):
    '''
    Choose the best station around the arrival and then define a trip
    between the departure and the station.
    '''
    city = situation['city']
    people = situation['people']
    time = tools.convert_time(situation['time'])
    # Convert the positions to (lat, lon) if they are textual addresses
    departure = geography.convert_to_point(city, situation['departure'])
    arrival = geography.convert_to_point(city, situation['arrival'])
    # Find the close stations with MongoDB and Hilbert curves
    stations = [station for station in
                geo.close_points(city, arrival, number=nbCandidates)]
    # Get the distances to the stations
    candidates = geography.compute_distances_manual(arrival, stations,
                                                    distance)
    # Sort the stations by distance
    candidates.sort(key=lambda station: station['duration'])
    # Find an appropriate solution through the sorted candidates
    trip = False
    for candidate in candidates:
        # Calculate what time it would be when reaching the candidate station
        currentTime = time + candidate['duration']
        currentTime = tools.epoch_to_datetime(time)
        # Check if the prediction is satisfying
        prediction = wrapper.predict('forest', currentTime, target,
                                     city, candidate['_id'])
        if prediction >= people:
            stationPosition = list(reversed(candidate['p']))
            if stationFirst is False:
                trip = reshape(mode, departure, stationPosition)
            else:
                trip = reshape(mode, stationPosition, departure)
            break
    return trip


def reshape(mode, A, B):
    ''' Format points into a convenient format. '''
    return {
        'mode': mode,
        'points': [
            {'lat': A[0], 'lon': A[1]},
            {'lat': B[0], 'lon': B[1]}
        ]
    }


@tools.MWT(timeout=60*60*24)
def get_route(url):
    ''' Specific function to perform caching. '''
    data = tools.query_API(url, repeat=False)
    return data


def generate_route(trip):
    ''' Build a path using the Mapzen's Valhalla API. '''
    mode = trip['mode']
    points = trip['points']
    base = 'http://valhalla.mapzen.com/'
    key = tools.read_json('config/keys.json')['valhalla']
    request = json.dumps({
        'locations': points,
        # 'costing': mode,
        # For some reasons the biking costing is not close to reality
        'costing': 'pedestrian',
        'directions_options': {
            'units': 'kilometers'
        }
    })
    url = '{0}route?json={1}&api_key={2}'.format(base, request, key)
    # No whitespace allowed
    url = url.replace(' ', '')
    data = get_route(url)
    path = tools.load_json(data)
    return {'mode': mode, 'polyline': path['trip']['legs'][0]['shape'],
            'maneuvers': path['trip']['legs'][0]['maneuvers'],
            'distance': path['trip']['legs'][0]['summary']['length']}
