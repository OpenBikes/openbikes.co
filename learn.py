import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import time
from common import toolbox as tb
from mongo.timeseries import query
from learning import *

settings = tb.read_json('common/settings.json')
informationFolder = settings['folders']['information']
# Number of days to learn upon
timespan = settings['learning']['timespan']
# Number of days for rescheduling
refresh = settings['learning']['refresh']
# Regression method
method = eval(settings['learning']['method'])
# Stations to predict
stationsFile = tb.read_json('{}/stations.json'.format(informationFolder))
# Define which cities can be predicted or not
predictions = tb.read_json('{}/predictions.json'.format(informationFolder))


def learn(city, station):
    # Get data from the past 30 days
    threshold = datetime.datetime.now() - datetime.timedelta(days=timespan)
    try:
        dataframe = query.station(city, station, threshold)
    except:
        return
    # Prepare the dataframe for learning
    dataframe = munging.prepare(dataframe)
    # Apply the regressor that is chosen in the settings
    method.fit(dataframe, 'bikes', city, station)
    method.fit(dataframe, 'spaces', city, station)

if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    for city in stationsFile.keys():
        if predictions[city] == 'Yes':
            for station in stationsFile[city]:
                learn(city, station)
                scheduler.add_job(learn, 'interval', days=refresh,
                                  args=[city, station], coalesce=True,
                                  misfire_grace_time=60*60*24*refresh)
    scheduler.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
