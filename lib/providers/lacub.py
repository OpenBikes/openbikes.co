from lib import tools

def stations(city):
    # The city parameter is necessary so that everything works
    key = tools.read_json('config/keys.json')['lacub']
    url = 'http://data.lacub.fr/wfs?key={}' \
          '&SERVICE=WFS&VERSION=1.1.0&' \
          'REQUEST=GetFeature' \
          '&TYPENAME=CI_VCUB_P&SRSNAME=EPSG:4326'
    print(url)
    data = tools.query_API(url)
    stations = tools.load_xml(data)
    print(stations)
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
