from datetime import datetime
from common import toolbox as tb


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'http://minaport.ubweb.jp/stations.php'
    data = tb.query_API(url)
    stations = tb.load_xml(data)
    return normalize(stations)


def normalize(stations):
    extract = tb.extract_attribute
    normalized = lambda station: {
        'name': extract(station, 'stname'),
        'address': extract(station, 'staddr'),
        'lat': float(extract(station, 'stlat')),
        'lon': float(extract(station, 'stlng')),
        'status': 'CLOSED' if extract(station, 'stat1') == '0'
                  and extract(station, 'stat2') == '0' else 'OPEN',
        'bikes': int(extract(station, 'stat1')),
        'stands': int(extract(station, 'stat2')),
        'update': datetime.strptime(extract(station, 'date'),
                                    '%Y-%m-%d %H:%M:%S').isoformat()
    }
    return [normalized(station) for station
            in stations.find_all('marker')]
