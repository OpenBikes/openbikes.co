from common import toolbox as tb


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'https://www.capitalbikeshare.com/data/stations/bikeStations.xml'
    data = tb.query_API(url)
    stations = tb.load_xml(data)
    return normalize(stations)


def normalize(stations):
    extract = tb.extract_element
    normalized = lambda station: {
        'name': extract(station, 'name'),
        'address': extract(station, 'name'),
        'lat': float(extract(station, 'lat')),
        'lon': float(extract(station, 'long')),
        'status': 'OPEN' if extract(station, 'locked') == 'false' else 'CLOSED',
        'bikes': int(extract(station, 'nbbikes')),
        'stands': int(extract(station, 'nbemptydocks')),
        'update': tb.epoch_to_datetime(int(extract(station,
                                           'latestupdatetime')),
                                       divisor=1000).isoformat()
    }
    return [normalized(station) for station
            in stations.find_all('station')]
