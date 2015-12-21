import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from collecting.providers import *
from mongo.timeseries import insert
from common import toolbox as tb

settings = tb.read_json('common/settings.json')
# Where to save the geojson files
geojsonFolder = settings['folders']['geojson']
# Where to place the updated timestamps
informationFolder = settings['folders']['information']
# Seconds for rescheduling
refresh = settings['collecting']['refresh']
# List of data providers
providers = tb.read_json('{}/providers.json'.format(informationFolder))
# Define which cities can be predicted or not
predictions = tb.read_json('{}/predictions.json'.format(informationFolder))


def update(provider, city, predict):
    ''' Update the data for a city. '''
    # Get the current formatted data for a city
    try:
        stations = eval(provider).stations(city)
    except:
        return
    # Update the database if the city can be predicted
    if predict == 'Yes':
        insert.city(city, stations)
    # Save the data for the map
    geojson = tb.json_to_geojson(stations)
    tb.write_json(geojson, '{0}/{1}.geojson'.format(geojsonFolder, city))
    # Refresh the latest update time
    updates = tb.read_json('{}/updates.json'.format(informationFolder))
    updates[city] = datetime.now().isoformat()
    tb.write_json(updates, '{}/updates.json'.format(informationFolder))

if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    for provider, cities in providers.items():
        for city in cities:
            update(provider, city, predictions[city])
            scheduler.add_job(update, 'interval', seconds=refresh,
                              args=[provider, city, predictions[city]],
                              misfire_grace_time=refresh, coalesce=True)
    scheduler.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
