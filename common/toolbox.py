from urllib.request import urlopen
from datetime import datetime
import pandas
import json
import os
import unicodedata
from bs4 import BeautifulSoup
import time


def json_to_geojson(json):
    ''' Convert to a format readable by Leaflet. '''
    geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [entry['lon'], entry['lat']]
                },
                'properties': entry,
            } for entry in json]
    }
    return geojson


def epoch_to_datetime(epoch, divisor=1):
    ''' Convert a UNIX timestamp to ISO formatted time. '''
    time = datetime.fromtimestamp(round(epoch / divisor))
    return time


def iso_account_AM_PM(isoDate):
    ''' Account for the AM/PM notation of an ISO formatted date '''
    timestamp = datetime.strptime(isoDate, '%Y-%m-%d %I:%M:%S %p')
    iso = timestamp.isoformat()
    return iso


def write_json(dictionary, filename):
    ''' Saves a dictionary to a JSON file. '''
    with open(filename, 'w') as outfile:
        json.dump(dictionary, outfile)


def read_json(file):
    ''' Open a JSON file and loads it as a dictionary. '''
    with open(file) as infile:
        dictionary = load_json(infile.read())
        return dictionary


def load_json(string):
    ''' Convenience wrapper for the json library. '''
    return json.loads(string)


def load_xml(string):
    ''' Convenience wrapper for the BeautifulSoup library. '''
    return BeautifulSoup(string, 'lxml')


def extract_element(element, child):
    '''
    Extract the content of a child element from an XML element.
    '''
    value = element.find(child)
    if type(value) is None:
        return ''
    elif not value:
        return ''
    else:
        return value.string


def extract_attribute(element, attribute):
    ''' Extract an attribute from an XML element. '''
    value = element.get(attribute)
    return value


def remove_special_characters(string):
    ''' Remove special characters such as accents. '''
    text = unicodedata.normalize('NFKD', string)
    cleanBytes = text.encode('ascii', 'ignore')
    cleanText = cleanBytes.decode('utf-8')
    return cleanText


def normalize_string(string):
    ''' Clean a string for caching purposes. '''
    string = string.lower()
    string = string.lstrip()
    string = string.rstrip()
    string = ' '.join(string.split())
    return string


def reshape(mode, A, B):
    ''' Format points into a convenient format. '''
    return {
        'mode': mode,
        'points': [
            {'lat': A[0], 'lon': A[1]},
            {'lat': B[0], 'lon': B[1]}
        ]
    }


class MWT(object):
    ''' Memoize With Timeout. '''
    _caches = {}
    _timeouts = {}

    def __init__(self, timeout=2):
        self.timeout = timeout

    def collect(self):
        ''' Clear cache of results which have timed out. '''
        for func in self._caches:
            cache = {}
            for key in self._caches[func]:
                if (time.time() - self._caches[func][key][1]) < self._timeouts[func]:
                    cache[key] = self._caches[func][key]
            self._caches[func] = cache

    def __call__(self, f):
        self.cache = self._caches[f] = {}
        self._timeouts[f] = self.timeout

        def func(*args, **kwargs):
            kw = sorted(kwargs.items())
            key = (args, tuple(kw))
            try:
                v = self.cache[key]
                if (time.time() - v[1]) > self.timeout:
                    raise KeyError
            except KeyError:
                v = self.cache[key] = (f(*args, **kwargs), time.time())
            return v[0]
        func.func_name = f.__name__
        return func


def query_API(url, repeat=False, encoding='utf-8'):
    ''' Send a query to a URL and decode the bytes it returns. '''
    if repeat is False:
        with urlopen(url) as response:
            return response.read().decode(encoding)
    # Possibility to continuously re-qeury the API if it failed
    else:
        response = None
        while response is None:
            try:
                with urlopen(url) as response:
                    return response.read().decode(encoding)
            except:
                response = None


@MWT(timeout=60 * 60 * 24)
def query_API_cached(url):
    ''' Convenience function in order to perform caching. '''
    response = query_API(url)
    return response
