from common import toolbox as tb
from common import keys


def weather(city):
    base = 'http://api.openweathermap.org/data/2.5/weather?q='
    key = keys.openweathermap
    url = '{0}{1}&units=metric&APPID={2}'.format(base, city, key)
    data = tb.query_API(url)
    owm_weather = tb.load_json(data)

    weather = {
        'datetime': tb.epoch_to_datetime(owm_weather['dt']).isoformat(),
        'pressure': owm_weather['main']['pressure'],
        'weather': owm_weather['weather'][0]['main'],
        'description': owm_weather['weather'][0]['description'],
        'temp': owm_weather['main']['temp'],
        'humidity': owm_weather['main']['humidity'],
        'wind_speed': owm_weather['wind']['speed'],
        'wind_dir': owm_weather['wind']['deg'],
        'rain_vol': owm_weather['rain']['3h'],
        'snow_vol': owm_weather['snow']['3h'] if 'snow' in owm_weather else 0,
        'clouds_pct': owm_weather['clouds']['all'],
    }
    return weather
