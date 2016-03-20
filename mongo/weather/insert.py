from mongo.weather import db

# 'i': information
# 'p': pressure
# 't': temperature
# 'h': humidity
# 'w': wind speed
# 't': temperature
# 'c': clouds


def city(city, weather):
    ''' Add the latest weather update for a city. '''
    # Connect to the appropriate collection of the database
    collection = db[city]
    # Extract the date
    date = weather['datetime'].date().isoformat()
    time = weather['datetime'].time().isoformat()
    # Check the day has already been inserted
    if collection.find({'_id': date}, {'_id': 1}).count() == 0:
        collection.save({
            '_id': date,
            'u': []
        })
    # Update the day with the new information
    collection.update({'_id': date}, {
        '$addToSet': {
            'u.$.m': time
            'u.$.i': {
                'p': weather['pressure'],
                't': weather['temperature'],
                'h': weather['humidity'],
                'w': weather['wind_speed'],
                'c': weather['clouds']
            }
        }
    })
