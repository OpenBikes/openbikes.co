from common import toolbox as tb


def stations(city):
    cities_uid = {
        'Warszawa': 210,
        'Riga': 128,
        'Jurmala': 140,
        'Wroclaw': 148,
        'Seferihisar': 249,
        'Dubai': 219,
        'AbuDhabi': 322,
        'Zagreb': 220,
        'Krakow': 232,
        'Bialystok': 245,
        'Belfast': 238,
        'KonstancinJeziorna': 247,
        'Sibenik': 248,
        'Lublin': 251,
        'GrodziskMazowiecki': 255,
        'Pittsburgh': 254,
        'Heidelberg': 194,
        'WestPalmBeachFlorida': 283,
        'Auckland': 34,
        'Christchurch': 193
    }
    uid = cities_uid[city]
    url = 'https://nextbike.net/maps/nextbike-official.xml?city={}'.format(uid)
    data = tb.query_API(url)
    print(url)
    stations = tb.load_xml(data)
    return normalize(stations)


def normalize(stations):
    extract = tb.extract_element
    normalized = lambda station: {
        'name': station['name'],
        'address': station['name'],
        'lat': float(station['lat']),
        'lon': float(station['lng']),
        'status': 'OPEN' if station['bike_racks'] != 0 and station['bikes'] != 0 else 'CLOSED',
        'bikes': int(station['bike_racks']) if not 'free_racks' in station else int(station['bike_racks']) - int(station['free_racks']),
        'stands': 0 if not 'free_racks' in station else int(station['free_racks'])
    }
    return [normalized(dict(station.attrs)) for station
            in stations.find_all('place')]
