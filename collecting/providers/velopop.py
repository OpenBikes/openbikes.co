from common import toolbox as tb


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'http://www.velopop.fr/vcstations.xml'
    data = tb.query_API(url, encoding='latin-1')
    stations = tb.load_xml(data)
    return normalize(stations)


def normalize(stations):
    extract = tb.extract_element
    normalized = lambda station: {
        'name': station['na'],
        'address': station['na'],
        'lat': float(station['la']),
        'lon': float(station['lg']),
        'status': 'OPEN',
        'bikes': int(station['av']),
        'stands': int(station['fr'])
    }
    return [normalized(dict(station.attrs)) for station
            in stations.find_all('si')]
