from datetime import timedelta
from common import toolbox as tb
from common import files, settings

# Configure celery
CELERY_RESULT_BACKEND = 'mongodb'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'host': '127.0.0.1',
    'port': 27017,
    'database': 'OpenBikes_Celery_Tasks',
    'taskmeta_collection': 'Tasks',
}
BROKER_URL = 'mongodb://localhost:27017/OpenBikes_Celery_Broker'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']

# Add tasks
CELERYBEAT_SCHEDULE = {}

# Providers file
providers = tb.read_json(files.providers)
# Predictions file
predictions = tb.read_json(files.predictions)
# Stations file
stations = tb.read_json(files.stations)

# City data collection
for provider, cities in providers.items():
    for city in cities:
        task_name = 'Collect_{0}'.format(city)
        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'tasks.update',
            'schedule': timedelta(seconds=settings.collecting['refresh']),
            'args': (provider, city, predictions[city])
        }

# Station regressors training
for city in stations.keys():
    if predictions[city] == 'Yes':
        for station in stations[city]:
            task_name = 'Learn_{0}_{1}'.format(city, station)
            CELERYBEAT_SCHEDULE[task_name] = {
                'task': 'tasks.learn',
                'schedule': timedelta(seconds=settings.learning['refresh']),
                'args': (provider, city)
            }
