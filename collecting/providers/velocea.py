from common import toolbox as tb
import re
import datetime


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'https://www.velocea.fr/cartoV2/libProxyCarto.asp'
    data = tb.query_API(url)
    stations = tb.load_json(data)
    return normalize(stations)


def clean(s):
    s = s.replace("+", " ")
    s = s.replace("%c3%b4", "ô")
    s = s.replace("%c3%a9", "é")
    return s


def normalize(stations):
    metadata = stations
    stations = stations['stand']
    normalized = lambda station: {
        'name': clean(station['name']),
        'address': clean(station['name']),
        'lat': float(station['lat']),
        'lon': float(station['lng']),
        'status': 'OPEN' if station['disp'] == '1' else 'CLOSED',
        'bikes': int(station['ab']),
        'stands': int(station['ap']),
        'update': datetime.datetime.strptime(metadata['gmt'], '{dt.day}/%m/%Y %H:%M:%S %p').isoformat()}
    return [normalized(station) for station in stations]
