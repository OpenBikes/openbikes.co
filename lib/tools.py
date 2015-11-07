from urllib.request import urlopen
from datetime import datetime
import pandas
import json
import os
import unicodedata
from bs4 import BeautifulSoup
import pickle
from zipfile import ZipFile
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


def query_API(url, repeat=False):
    ''' Send a query to a URL and decode the bytes it returns. '''
    if repeat is False:
        with urlopen(url) as response:
            return response.read().decode('utf-8')
    # Possibility to continuously re-qeury the API if it failed
    else:
        response = None
        while response is None:
            try:
                with urlopen(url) as response:
                    return response.read().decode('utf-8')
            except:
                response = None


def dump_json(dictionary, fileName):
    ''' Saves a dictionary to a JSON file. '''
    with open(fileName, 'w') as outfile:
        json.dump(dictionary, outfile)


def read_json(file):
    ''' Open a JSON file and loads it as a dictionary. '''
    with open(file) as infile:
        dictionary = load_json(infile.read())
        return dictionary


def load_json(string):
    return json.loads(string)


def load_xml(string):
    return BeautifulSoup(string, 'lxml')


def extract_element(element, child):
    '''
    Extract the content of a child element from an XML element.
    '''
    value = element.find(child)
    if type(value) is None:
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


def dict_to_dataframe(dict):
    ''' Converts a dictionary into a dataframe. '''
    # Extract the information
    dataframe = pandas.DataFrame(dict)
    # Return it as a dataframe where every row is an update
    return dataframe


def convert_time(time):
    ''' Convert the time the user chose into a Datetime object. '''
    # It's either now
    if len(time) == 1:
        newTime = time[0] / 1000
    # Or defined by the user
    else:
        newTime = epoch_to_datetime(time[0], divisor=1000)
        hour, minute = time[1].split(':')
        newTime = newTime.replace(hour=int(hour), minute=int(minute))
        newTime = newTime.timestamp()
    return round(newTime)


def save_predictor(predictor, method, target, city, station):
    ''' Save a predictor with pickle. '''
    directory = 'predictors/{0}/{1}/{2}'.format(method, target, city)
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = '{0}/{1}'.format(directory, station.replace('/', '_'))
    # Destroy the zipfile if it already exists
    try:
        os.remove('{0}.zip'.format(path))
    except:
        pass
    # Save the predictor
    with open('{0}.pkl'.format(path), 'wb') as outfile:
        pickle.dump(predictor, outfile)
    # Zip it
    with ZipFile('{0}.zip'.format(path), 'w') as zipped:
        zipped.write('{0}.pkl'.format(path))
    # Destroy it
    os.remove('{0}.pkl'.format(path))


def load_predictor(method, target, city, station):
    ''' Load a predictor with pickle. '''
    path = 'predictors/{0}/{1}/{2}/{3}'.format(method, target, city,
                                               station.replace('/', '_'))
    with ZipFile('{0}.zip'.format(path)) as zf:
        zf.extractall()
    with open('{0}.pkl'.format(path), 'rb') as infile:
        os.remove('{0}.pkl'.format(path))
        predictor = pickle.load(infile)
        return predictor


def normalize_string(string):
    ''' Clean a string for caching purposes. '''
    string = string.lower()
    string = string.lstrip()
    string = string.rstrip()
    string = ' '.join(string.split())
    return string


def euclidian_distance(p1, p2):
    a = (p1[0] - p2[0]) ** 2
    b = (p1[1] - p2[1]) ** 2
    return (a + b) ** (1 / 2)


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
