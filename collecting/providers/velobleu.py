from common import toolbox as tb
import re
import datetime


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'http://www.velobleu.org/cartoV2/libProxyCarto.asp'
    data = tb.query_API(url)
    stations = tb.load_json(data)
    return normalize(stations)


def clean(s):
    if s is not None:
        s = s.replace("+", " ")
        s = s.replace("%c3%a0", "à")
        s = s.replace("%c2%b0", "°")
        s = s.replace("%c3%a9", "é")
        s = s.replace("%c3%a7", "ç")
        s = s.replace("%27", "'")
        s = s.replace("%e2%80%99", "è")
        s = s.replace("%c3%a8", "'")
        s = s.replace("%c3%ae", "î")
        s = s.upper()
        return s


def normalize(stations):
    metadata = stations
    stations = stations['stand']
    normalized = lambda station: {
        'name': clean(str(station['wcom']) + str(station['name'])),
        'address': clean(station['name']),
        'lat': float(station['lat']),
        'lon': float(station['lng']),
        'status': 'OPEN' if station['disp'] == '1' else 'CLOSED',
        'bikes': int(station['ab']),
        'stands': int(station['ap']),
        'update': datetime.datetime.strptime(metadata['gmt'], '%d/%m/%Y %H:%M:%S %p').isoformat()}
    return [normalized(station) for station in stations]
