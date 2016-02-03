from routing import geography
from common import toolbox as tb
from mongo.geo import query
from learning import *


def choose_station(situation, address, target, distance, mode, stationFirst, nbCandidates=5):
    '''
    Choose the best station around the arrival and then define a trip
    between the departure and the station.
    '''
    city = situation['city']
    people = situation['people']
    time = tb.convert_time(situation['time'])
    # Will convert the positions to (lat, lon) if they are textual addresses
    point = geography.convert_to_point(city, address)
    # Find the close stations with MongoDB
    stations = [station for station in
                query.close_points(city, point, number=nbCandidates)]
    # Get the distances to the stations

    candidates = geography.compute_distances_manual(point, stations, distance)

    # Sort the stations by distance
    candidates.sort(key=lambda station: station['duration'])
    # Find an appropriate solution through the sorted candidates
    trip = False
    for candidate in candidates:
        # Calculate what time it would be when reaching the candidate station
        forecast = tb.epoch_to_datetime(time + candidate['duration'])
        # Extract features from the forecasted time
        variables = munging.temporal_features(forecast)
        features = [variables['hour'], variables['minute'],
                    variables['weekday']]
        # Make a prediction
        settings = tb.read_json('common/settings.json')
        method = eval(settings['learning']['method'])
        prediction = method.predict(features, target, city, candidate['_id'])
        bias = tb.read_json('common/settings.json')['learning']['bias']
        if target == 'bikes':
            bias *= -1
        if prediction + bias >= people:
            stationPosition = list(reversed(candidate['p']))
            if stationFirst is False:
                trip = tb.reshape(mode, departure, stationPosition)
            else:
                trip = tb.reshape(mode, stationPosition, departure)
            break
    return trip


@tb.MWT(timeout=60*60*24)
def get_route(url):
    ''' Specific function to perform caching. '''
    response = tb.query_API(url)
    return response


def turn_by_turn(trip):
    ''' Build a path using the Google Directions API. '''
    mode = trip['mode']
    points = [
        '{0},{1}'.format(point['lat'], point['lon'])
        for point in trip['points']
    ]
    origin = points[0]
    destination = points[1]
    base = 'https://maps.googleapis.com/maps/api/directions/json'
    key = tb.read_json('common/keys.json')['google-distance']
    url = '{0}?origin={1}&destination={2}&mode={3}&key={4}'.format(base,
                                                                   origin,
                                                                   destination,
                                                                   'walking',
                                                                   key)
    # Query the API
    response = get_route(url)
    trip = tb.load_json(response)
    return {
        'mode': mode,
        'routes': trip['routes'][0]['legs'][0]['steps'],
        'polyline': trip['routes'][0]['overview_polyline']['points']
    }
