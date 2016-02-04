import datetime
from mongo.timeseries import query
from learning import munging

city = 'Toulouse'
station = '00067 - MUSEUM'
threshold = datetime.datetime.now() - datetime.timedelta(days=3)

dataframe = query.station(city, station, threshold)
dataframe = munging.prepare(dataframe)

X, Y = munging.split(dataframe, 'bikes')
