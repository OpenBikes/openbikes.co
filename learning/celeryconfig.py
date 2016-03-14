#!/usr/bin/python3
from celery.schedules import crontab
from common import toolbox as tb
from common import files

# Configure celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IGNORE_RESULT = True
CELERY_DISABLE_RATE_LIMITS = True

# Use RabbitMQ
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# Add tasks
CELERYBEAT_SCHEDULE = {}

# Predictions file
predictions = tb.read_json(files.predictions)
# Stations file
stations = tb.read_json(files.stations)


# Station regressors training
for city, stations in stations.items():
    if predictions[city] == 'Yes':
        task_name = 'Learn_{0}'.format(city)
        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'learn.learn',
            # Every monday at 2 o'clock
            'schedule': crontab(hour=2, minute=0, day_of_week='wednesday'),
            'args': (city, stations)
        }
