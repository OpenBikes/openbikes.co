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

# City data collection
for provider, cities in providers.items():
    for city in cities:
        task_name = 'Collect_{0}'.format(city)
        CELERYBEAT_SCHEDULE[task_name] = {
            'task': 'collect.collect',
            'schedule': timedelta(seconds=settings.collecting['refresh']),
            'args': (provider, city, predictions[city])
        }
