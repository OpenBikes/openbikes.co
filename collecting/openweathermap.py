import requests
from common import toolbox as tb
from common import keys

def weather(city):
    '''
    Collect the weather data for a city. The city parameter corresponds to the
    name of the city in the OpenWeatherMap database, this makes results more
    reliable.
    '''
    base = 'http://api.openweathermap.org/data/2.5/weather?q='
    key = keys.openweathermap
    url = '{0}{1}&units=metric&APPID={2}'.format(base, city, key)
    owm_weather = requests.get(url).json()
    weather = {
        'datetime': tb.epoch_to_datetime(owm_weather['dt']),
        'pressure': owm_weather['main']['pressure'],
        'description': owm_weather['weather'][0]['description'],
        'temperature': round(owm_weather['main']['temp'], 2),
        'humidity': owm_weather['main']['humidity'],
        'wind_speed': owm_weather['wind']['speed'],
        'clouds': owm_weather['clouds']['all']
    }
    return weather
