#!/usr/bin/python3
from datetime import timedelta
from celery.schedules import crontab
from common import toolbox as tb
from common import files, settings

# Configure celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IGNORE_RESULT = True
CELERY_DISABLE_RATE_LIMITS = True

# Use RabbitMQ
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# Define different queues
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = {
    'default': {
        'exchange': 'default',
        'binding_key': 'default',
    },
    'q_collect': {
        'exchange': 'q_collect',
        'routing_key': 'q_collect',
    },
    'q_learn': {
        'exchange': 'q_learn',
        'routing_key': 'q_learn',
    }
}

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
            'args': (provider, city, predictions[city]),
            #'options': {'queue' : 'q_collect'}
        }

# Station regressors training
for city in stations.keys():
    if predictions[city] == 'Yes':
        for station in stations[city]:
            task_name = 'Learn_{0}_{1}'.format(city, station)
            CELERYBEAT_SCHEDULE[task_name] = {
                'task': 'tasks.learn',
                # Every monday at 2 o'clock
                'schedule': crontab(hour=2, minute=0, day_of_week='monday'),
                'args': (provider, city),
                #'options': {'queue' : 'q_learn'}
            }
