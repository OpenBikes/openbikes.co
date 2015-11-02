from apscheduler.schedulers.background import BackgroundScheduler
from lib.mongo import timeseries
from lib.learning import munging
from lib.learning import forest
from lib import tools
import time

stationsFile = tools.read_json('static/stations.json')

def learn(city):
    for station in stationsFile[city]:
        # Get all the data from the database
        dataframe = timeseries.query_station(city, station)
        # Prepare the dataframe for learning
        dataframe = munging.rename_columns(dataframe)
        dataframe = munging.prepare(dataframe)
        # Apply a regressor
        forest.fit(dataframe, 'bikes', city, station)
        forest.fit(dataframe, 'spaces', city, station)
    #timeseries.delete_city(city)
            
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    for city in stationsFile.keys():
        learn(city)
        scheduler.add_job(learn, 'interval', weeks=2, args=[city],
                          misfire_grace_time=60*60*24*7, coalesce=True)
    scheduler.start()
    while True:
        time.sleep(10e-1000000)