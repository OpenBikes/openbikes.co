from lib import tools
from datetime import datetime


def stations(city):
    # The city parameter is necessary so that everything works
    base = 'http://data.keolis-rennes.com/json/?version=1.0&'
    key = tools.read_json('config/keys.json')['keolis']
    url = '{0}key={1}&cmd=getstation'.format(base, key)
    data = tools.query_API(url)
    stations = tools.load_json(data)
    return normalize(stations)


def normalize(stations):
    stations = stations['opendata']['answer']['data']['station']
    normalized = lambda station: {
        'name': station['name'],
        'address': station['name'],
        'lat': float(station['latitude']),
        'lon': float(station['longitude']),
        'status': 'OPEN' if station['state'] == '1' else 'CLOSED',
        'bikes': int(station['bikesavailable']),
        'stands': int(station['slotsavailable']),
        'update': datetime.strptime(station['lastupdate'].split('+')[0],
                                    '%Y-%m-%dT%H:%M:%S').isoformat()
    }
    return [normalized(station) for station in stations]
