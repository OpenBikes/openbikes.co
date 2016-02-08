from common import toolbox as tb


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'http://www.decobike.com/playmoves.xml'
    data = tb.query_API(url)
    stations = tb.load_xml(data)
    return normalize(stations)


def normalize(stations):
    extract = tb.extract_element
    normalized = lambda station: {
        'name': extract(station, 'id') + " - " + extract(station, 'address'),
        'address': extract(station, 'address'),
        'lat': float(extract(station, 'latitude')),
        'lon': float(extract(station, 'longitude')),
        'status': 'OPEN' if extract(station, 'address').lower() != 'not in service' else 'CLOSED',
        'bikes': int(extract(station, 'bikes')),
        'stands': int(extract(station, 'dockings'))
    }
    return [normalized(station) for station
            in stations.find_all('location')]
