#!/usr/bin/python3
from datetime import timedelta
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

# Add tasks
CELERYBEAT_SCHEDULE = {}

# Providers file
providers = tb.read_json(files.providers)
# Predictions file
predictions = tb.read_json(files.predictions)
# OpenWeatherMap file
owm = tb.read_json(files.owm)


# City data collection
for provider, cities in providers.items():
    for city in cities:
        CELERYBEAT_SCHEDULE['Bikes_{0}'.format(city)] = {
            'task': 'collect.bikes',
            'schedule': timedelta(seconds=settings.collecting['bikes']),
            'args': (provider, city, predictions[city])
        }
        if predictions[city] == 'Yes':
            CELERYBEAT_SCHEDULE['Weather_{0}'.format(city)] = {
                'task': 'collect.weather',
                'schedule': timedelta(seconds=settings.collecting['weather']),
                'args': (city, owm[city])
            }
