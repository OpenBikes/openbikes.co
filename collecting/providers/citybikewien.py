from common import toolbox as tb


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'http://dynamisch.citybikewien.at/citybike_xml.php'
    data = tb.query_API(url)
    stations = tb.load_xml(data)
    return normalize(stations)


def normalize(stations):
    normalized = lambda station: {
        'name': station.find('name').string,
        'address': station.find('description').string,
        'lat': float(station.find('latitude').string),
        'lon': float(station.find('longitude').string),
        'status': 'OPEN' if station.find('status').string == 'aktiv' else 'CLOSED',
        'bikes': int(station.find('free_bikes').string),
        'stands': int(station.find('free_boxes').string)
    }
    return [normalized(station) for station
            in stations.find_all('station')]
