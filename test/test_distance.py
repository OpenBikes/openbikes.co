import datetime
from mongo.geo import query
from common import toolbox as tb

city = 'Toulouse'

mode = 'bicycling'

time = (datetime.datetime.now() + datetime.timedelta(hours=1)).timestamp()

# Université Paul Sabatier, Toulouse
point = (43.594348, 1.45037562729196)

stations = [station for station in query.close_points(city, point, number=5)]


base = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
key = tb.read_json('common/keys.json')['google-distance']
origin = '{lat},{lon}'.format(lat=point[0], lon=point[1])
destinations = '|'.join(['{lat},{lon}'.format(lat=station['p'][1], lon=station['p'][0])
                         for station in stations])
url = '{0}mode={1}&key={2}&origins={3}&destinations={4}&time={5}'.format(base, mode, key, origin, destinations, time)
response = tb.query_API_cached(url)
trip = tb.load_json(response)
