# Testing

Toulouse is the *de facto* city for running tests. As such Toulouse data should be collected and regressors trained. In any case these steps have to be performed during functional testing.

## Functional tests

### Collecting data with Celery

- Boot RabbitMQ with `rabbitmq-server -detached`
- Collect data with `celery -A collect worker --beat --loglevel=info`
- Cleanse Celery with `celery purge`

### Training the regressors

`python learn.py`

## Unit tests

- [API](testing/test_api.py)
