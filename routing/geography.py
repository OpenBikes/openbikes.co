from common import toolbox as tb


@tb.MWT(timeout=60*60*24)
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


def convert_to_point(city, address):
    '''
    Convert an address to [lat, lon] with Nominatim, if
    the input is already [lat, lon] then don't do anything
    (the user decided to use his current position).
    '''
    if isinstance(address, str):
        address = '{0} {1}'.format(city, address)
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
    ''' Just Euclidian distance, good approximation nonetheless. '''
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
