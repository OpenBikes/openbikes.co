from mongo.weather import db

# 'i': information
# 'd': description
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
    # Check the dates has already been inserted
    if collection.find({'_id': date}, {'_id': 1}).count() == 0:
        collection.save({
            '_id': date,
            'u': []
        })
    # Add the entry if it doesn't exist and there is data
    if collection.find({'_id': date, 'u.m': time}).limit(1).count() == 0:
        # Update the day with the new information
        collection.update({'_id': date}, {
            '$addToSet': {
                'u': {
                    'm': time,
                    'd': weather['description'],
                    'p': weather['pressure'],
                    't': weather['temperature'],
                    'h': weather['humidity'],
                    'w': weather['wind_speed'],
                    'c': weather['clouds']
                }
            }
        })
