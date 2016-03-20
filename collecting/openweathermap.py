from common import toolbox as tb
from common import keys


def weather(city, city_id):
    '''
    Collect the weather data for a city. The city_id corresponds to the name
    of the city in the OpenWeatherMap database, this makes results more
    reliable.
    '''
    base = 'http://api.openweathermap.org/data/2.5/weather?q='
    key = keys.openweathermap
    url = '{0}{1}&units=metric&APPID={2}'.format(base, city, key)
    data = tb.query_API(url)
    owm_weather = tb.load_json(data)
    weather = {
        'datetime': tb.epoch_to_datetime(owm_weather['dt']),
        'pressure': owm_weather['main']['pressure'],
        'description': owm_weather['weather'][0]['description'],
        'temperature': owm_weather['main']['temp'],
        'humidity': owm_weather['main']['humidity'],
        'wind_speed': owm_weather['wind']['speed'],
        'clouds': owm_weather['clouds']['all']
    }
    return weather
