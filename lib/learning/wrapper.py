from lib.learning import munging
from lib.learning import (
    forest
)

def predict(method, time, target, city, station):
    variables = {
        'time': time
    }
    variables.update(munging.temporal_features(variables['time']))
    del variables['time']
    features = [variables['hour'], variables['minute'],
                variables['weekday']]
    return eval(method).predict(features, target, city, station)