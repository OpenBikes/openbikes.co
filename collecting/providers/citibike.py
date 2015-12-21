from common import toolbox as tb


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'https://www.citibikenyc.com/stations/json'
    data = tb.query_API(url)
    stations = tb.load_json(data)
    return normalize(stations)


def normalize(stations):
    stations = stations['stationBeanList']
    normalized = lambda station: {
        'name': station['stationName'],
        'address': station['stAddress1'],
        'lat': station['latitude'],
        'lon': station['longitude'],
        'status': 'OPEN' if station['statusValue'] == 'In Service' else 'CLOSED',
        'bikes': int(station['availableBikes']),
        'stands': int(station['availableDocks']),
        'update': tb.iso_account_AM_PM(station['lastCommunicationTime'])
    }
    return [normalized(station) for station in stations]
