from mongo.timeseries import db


def city(city):
    ''' Destroy a collection. '''
    db.drop_collection(city)
