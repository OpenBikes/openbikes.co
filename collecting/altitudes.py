from common import toolbox as tb
from common import keys


def add(stations, size=50):
    '''
    Use the Google Maps Elevation API to add altitudes to a dataframe.
    Because the API has a limitation this function batches the work into
    "packages" that are successively send to the API. The size parameter
    determines the size of the packages. The function starts by looping
    through the stations and increments a counter. Once the counter has
    reached the package size then it sends a request to the API and resets the
    counter. Once it has parsed all the stations it unwraps what the API
    send back into a list of dictionaries and sends it back.
    '''
    base = 'https://maps.googleapis.com/maps/api/elevation/json?'
    key = keys.google_elevation
    locations = ''
    packages = []
    counter = 1
    for station in stations:
        locations += '{lat},{lon}|'.format(lat=station['lat'],
                                           lon=station['lon'])
        counter += 1
        if counter >= size:
            locations += ';'
            counter = 1
    for loc in locations.split(';'):
        url = base + 'locations={0}&key={1}'.format(loc[:-1], key)
        request = tb.query_API(url)
        data = tb.load_json(request)
        packages.append(data['results'])
    # Melt the packages into one list
    altitudes = []
    for package in packages:
        altitudes.extend(package)
    # Tidy everything up for database insertion
    data = [{'name': station[0]['name'], 'lat': station[0]['lat'],
             'lon': station[0]['lon'], 'alt': station[1]['elevation']}
            for station in zip(stations, altitudes)]
    return data
