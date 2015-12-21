from common import toolbox as tb
from collecting.providers import keys


def stations(city):
    base = 'https://api.jcdecaux.com/vls/v1/'
    key = keys['jcdecaux']
    url = '{0}stations/?contract={1}&apiKey={2}'.format(base, city, key)
    data = tb.query_API(url)
    stations = tb.load_json(data)
    return normalize(stations)


def normalize(stations):
    normalized = lambda station: {
        'name': station['name'],
        'address': station['address'],
        'lat': station['position']['lat'],
        'lon': station['position']['lng'],
        'status': station['status'],
        'bikes': station['available_bikes'],
        'stands': station['available_bike_stands'],
        'update': tb.epoch_to_datetime(station['last_update'],
                                       divisor=1000).isoformat()
    }
    return [normalized(station) for station in stations]
