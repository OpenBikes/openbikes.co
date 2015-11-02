from lib import tools

def add_altitudes(stations, size=50):
    ''' Use the Google Maps Elevation API. ''' 
    base = 'https://maps.googleapis.com/maps/api/elevation/json?'
    key = tools.read_json('config/keys.json')['google-elevation']
    locationsList = ''
    packages = []
    counter = 1
    for station in stations:
        locationsList += '{lat},{lon}|'.format(lat=station['lat'],
                                               lon=station['lon'])
        # The API only allows a certain amount of locations per request
        counter += 1
        if counter > size:
            locationsList += ';'
            counter = 1
    for locations in locationsList.split(';'):
        locations = locations[:-1]
        url = base + 'locations={0}&key={1}'.format(locations, key)
        request = tools.query_API(url)
        data = tools.load_json(request)
        packages.append(data['results'])
    # Melt the packages into one list
    altitudes = []
    for package in packages:
        altitudes.extend(package)
    # Tidy everything up for database insertion
    data = []
    for station in zip(stations, altitudes):
        data.append({
            'name': station[0]['name'],
            'lat': station[0]['lat'],
            'lon': station[0]['lon'],
            'alt': station[1]['elevation']
        })
    return data

@tools.MWT(timeout=60*60*24)
def geocode(address):
    '''
    Return the latitude and longitude of an address
    thanks to the Nominatim API.
    '''
    base = 'http://nominatim.openstreetmap.org/search?' \
           'format=json&polygon_geojson=1&q='
    text = tools.remove_special_characters(address)
    keywords = '+'.join(text.split())
    url = ''.join((base, keywords))
    data = tools.query_API(url)
    address = tools.load_json(data)[0]
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
        query = tools.normalize_string(address)
        point = geocode(query)
    else:
        point = address
    return point

def compute_distances(departure, stations, mode):
    ''' Using the Mapbox Distance API. '''
    # Interrogate the API to get the distance to each station
    base = 'https://api.mapbox.com/distances/v1/mapbox/'
    key = tools.read_json('config/keys.json')['mapbox-distance']
    coordinates = {
        'coordinates': [
            departure
        ] + [station['p'] for station in stations]
    }
    print(coordinates)
    # url = '{0}{1}?access_token={2}'.format(base, mode, key)
    #       base, origin, destinations, mode, key)
    # data = tools.query_API(url)
    # distances = tools.load_json(data)['rows'][0]['elements']
    # candidates = []
    # for station in zip(stations, distances):
    #     candidate = {}
    #     for information in station:
    #         candidate.update(information)
    #     candidates.append(candidate)
    # return candidates

def compute_distances_manual(departure, stations, mode):
    ''' Just Euclidian distance, useful for debugging. '''
    d = list(reversed(departure))
    distance = lambda s: ((s['p'][0] - d[0]) ** 2 + (s['p'][1] - d[1]) ** 2) ** (1/2)
    distances = [{'duration': distance(station)} for station in stations]
    candidates = []
    for station in zip(stations, distances):
        candidate = {}
        for information in station:
            candidate.update(information)
        candidates.append(candidate)
    return candidates




