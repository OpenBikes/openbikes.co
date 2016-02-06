from common import toolbox as tb


@tb.MWT(timeout=60 * 60 * 24)
def geocode(address):
    '''
    Return the latitude and longitude of an address
    thanks to the Nominatim API.
    '''
    base = 'http://nominatim.openstreetmap.org/search?' \
           'format=json&polygon_geojson=1&q='
    text = tb.remove_special_characters(address)
    keywords = '+'.join(text.split())
    url = ''.join((base, keywords))
    data = tb.query_API(url)
    address = tb.load_json(data)[0]
    latitude = float(address['lat'])
    longitude = float(address['lon'])
    return (latitude, longitude)


def convert_to_point(address):
    '''
    Convert an address to [lat, lon] with Nominatim, if
    the input is already [lat, lon] then don't do anything
    (the user decided to use his current position).
    '''
    if isinstance(address, str):
        query = tb.normalize_string(address)
        point = geocode(query)
    else:
        point = address
    return point


def euclidian_distance(p1, p2):
    a = (p1[0] - p2[0]) ** 2
    b = (p1[1] - p2[1]) ** 2
    return (a + b) ** (1 / 2)


def compute_distances_manual(departure, stations, mode):
    ''' Just Euclidian distance, useful for testing. '''
    d = list(reversed(departure))
    distances = [{'duration': euclidian_distance(station['p'], d)}
                 for station in stations]
    candidates = []
    for station in zip(stations, distances):
        candidate = {}
        for information in station:
            candidate.update(information)
        candidates.append(candidate)
    return candidates


def compute_distances(departure, stations, mode, time):
    ''' Using the Google Distance Matrix API. '''
    base = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    key = tb.read_json('common/keys.json')['google-distance']
    origin = '{lat},{lon}'.format(lat=departure[0], lon=departure[1])
    destinations = '|'.join(['{lat},{lon}'.format(lat=station['p'][1], lon=station['p'][0])
                             for station in stations])
    url = '{0}mode={1}&key={2}&origins={3}&destinations={4}&time={5}'.format(
        base, mode, key, origin, destinations, time)
    print(url)
    response = tb.query_API_cached(url)
    distances = tb.load_json(response)['rows'][0]['elements']
    # Add the distances to the stations
    for i, station in enumerate(stations):
        stations[i]['duration'] = distances[i]['duration']['value']
    return stations
