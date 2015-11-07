from apscheduler.schedulers.background import BackgroundScheduler
from lib.providers import wrapper
from lib.mongo import timeseries
from lib import tools
from datetime import datetime
import time
import json

providers = tools.read_json('static/providers.json')
centers = tools.read_json('static/centers.json')
predictions = tools.read_json('static/predictions.json')


def update(provider, city, predict):
    # Get the information for the city
    try:
        stations = wrapper.collect(provider, city)
    except:
        return
    # Update the database
    if predict == 'Yes':
        timeseries.update_city(stations, city)
    # Save the data for the map
    geojson = tools.json_to_geojson(stations)
    with open('static/geojson/{0}.geojson'.format(city), 'w') as outfile:
        json.dump(geojson, outfile)
    # Tell the server the city's data was updated
    with open('static/updates/{0}.txt'.format(city), 'w') as outfile:
        outfile.write(datetime.now().isoformat())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    for provider, cities in providers.items():
        for city in cities:
            time.sleep(3)
            update(provider, city, predictions[city])
            scheduler.add_job(update, 'interval', seconds=60,
                              args=[provider, city, predictions[city]],
                              misfire_grace_time=50, coalesce=True)
    scheduler.start()
    while True:
        time.sleep(10e-1000000)
