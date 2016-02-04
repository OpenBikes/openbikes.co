import datetime
from routing import handling

situation = {
    'mode': 'dropBike',
    'start': 'Université-Paul-Sabatier, Toulouse, France',
    'city': 'Toulouse',
    'people': 2,
    'time': datetime.datetime(2016, 2, 4, 18, 45).timestamp()
}

routes = handling.drop_bike(situation)
