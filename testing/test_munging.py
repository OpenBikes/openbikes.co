import datetime
from mongo.timeseries import query
from learning import munging

city = 'Toulouse'
station = '00067 - MUSEUM'
since = datetime.datetime.now() - datetime.timedelta(days=3)
until = datetime.datetime.now()

dataframe = query.station(city, station, since, until)
dataframe = munging.prepare(dataframe)

X, Y = munging.split(dataframe, 'bikes')
