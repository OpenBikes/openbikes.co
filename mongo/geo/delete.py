from mongo.geo import db


def city(city):
    ''' Delete a city entry. '''
    collection = db[city]
    collection.drop()
