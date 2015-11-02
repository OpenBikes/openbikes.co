from lib import tools

def stations(city):
    designations = {
        'Toronto': 'toronto',
        'Montréal': 'montreal',
        'Ottawa': 'capitale'
    }
    designation = designations[city]
    url = 'https://{}.bixi.com/data/bikeStations.xml'.format(designation)
    data = tools.query_API(url)
    stations = tools.load_xml(data)
    return normalize(stations)

def normalize(stations):
    extract = tools.extract_element
    normalized = lambda station: {
        'name': extract(station, 'name'),
        'address': extract(station, 'name'),
        'lat': float(extract(station, 'lat')),
        'lon': float(extract(station, 'long')),
        'status': 'OPEN' if extract(station, 'locked') == 'false'
                   else 'CLOSED',
        'bikes': int(extract(station, 'nbbikes')),
        'stands': int(extract(station, 'nbemptydocks')),
        'update': tools.epoch_to_datetime(int(extract(station,
                                                 'latestupdatetime')),
                                                 divisor=1000).isoformat()
    }
    return [normalized(station) for station
            in stations.find_all('station')]
