from common import toolbox as tb


def stations(city):
    # The city parameter is necessary so that everything works
    url = 'http://www.tashu.or.kr/mapAction.do?process=statusMapView'
    data = tb.query_API(url)
    stations = tb.load_json(data)
    return normalize(stations)


def normalize(stations):
    stations = stations['markers']
    normalized = lambda station: {
        'name': station['name'],
        'address': station['name'],
        'lat': float(station['lat']),
        'lon': float(station['lng']),
        'status': 'OPEN',
        'bikes': int(station['cntLockOff']),
        'stands': int(station['cntRentable']),
    }
    return [normalized(station) for station in stations]
