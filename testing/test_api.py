import json
from datetime import datetime as dt
from datetime import timedelta as td
from common import files
from common import toolbox as tb
from app.views.api import apibp
from app import app

client = app.test_client()
valid_city = 'Toulouse'
invalid_city = 'xyz'
valid_provider = 'jcdecaux'
invalid_provider = '123'
valid_country = 'France'
invalid_country = 'abc'
valid_station = '00003 - POMME'
invalid_station = '3.1415 - APPLE'


def json_response(response):
    ''' Shortcut for loading a response as a dictionary. '''
    return json.loads(response.data.decode('utf-8'))


def test_api_city_success():
    ''' Check api_city returns 'success' on valid city '''
    rv = client.get('/api/geojson/' + valid_city)
    assert json_response(rv)['status'] == 'success'


def test_api_city_failure():
    ''' Check api_city returns 'failure' on invalid city '''
    rv = client.get('/api/geojson/' + invalid_city)
    assert json_response(rv)['status'] == 'failure'


def test_api_stations_success():
    ''' Check api_stations returns 'success' on no city '''
    rv = client.get('/api/stations')
    assert json_response(rv)['status'] == 'success'


def test_api_stations_city_success():
    ''' Check api_stations returns 'success' on valid city '''
    rv = client.get('/api/stations/' + valid_city)
    assert json_response(rv)['status'] == 'success'


def test_api_stations_city_failure():
    ''' Check api_stations returns 'failure' on invalid city '''
    rv = client.get('/api/stations/' + invalid_city)
    assert json_response(rv)['status'] == 'failure'


def test_api_providers_success():
    ''' Check api_providers returns 'success' on no provider '''
    rv = client.get('/api/providers')
    assert json_response(rv)['status'] == 'success'


def test_api_providers_provider_success():
    ''' Check api_providers returns 'success' on valid provider '''
    rv = client.get('/api/providers/' + valid_provider)
    assert json_response(rv)['status'] == 'success'


def test_api_providers_provider_failure():
    ''' Check api_providers returns 'failure' on invalid provider '''
    rv = client.get('/api/providers/' + invalid_provider)
    assert json_response(rv)['status'] == 'failure'


def test_api_countries_success():
    ''' Check api_countries returns 'success' on no country '''
    rv = client.get('/api/countries')
    assert json_response(rv)['status'] == 'success'


def test_api_countries_country_success():
    ''' Check api_countries returns 'success' on valid country '''
    rv = client.get('/api/countries/' + valid_country)
    assert json_response(rv)['status'] == 'success'


def test_api_countries_provider_failure():
    ''' Check api_countries returns 'failure' on invalid country '''
    rv = client.get('/api/countries/' + invalid_country)
    assert json_response(rv)['status'] == 'failure'


def test_api_centers_success():
    ''' Check api_centers returns 'success' on no city '''
    rv = client.get('/api/centers')
    assert json_response(rv)['status'] == 'success'


def test_api_centers_city_success():
    ''' Check api_centers returns 'success' on valid city '''
    rv = client.get('/api/centers/' + valid_city)
    assert json_response(rv)['status'] == 'success'


def test_api_centers_city_failure():
    ''' Check api_centers returns 'failure' on invalid city '''
    rv = client.get('/api/centers/' + invalid_city)
    assert json_response(rv)['status'] == 'failure'


def test_api_updates_success():
    ''' Check api_updates returns 'success' on no city '''
    rv = client.get('/api/updates')
    assert json_response(rv)['status'] == 'success'


def test_api_updates_city_success():
    ''' Check api_centers returns 'success' on valid city '''
    rv = client.get('/api/updates/' + valid_city)
    assert json_response(rv)['status'] == 'success'


def test_api_updates_city_failure():
    ''' Check api_centers returns 'failure' on invalid city '''
    rv = client.get('/api/updates/' + invalid_city)
    assert json_response(rv)['status'] == 'failure'


def test_api_prediction_invalid_city():
    ''' Check api_prediction returns 'failure' on invalid city '''
    rv = client.get('/api/prediction/{city}/{station}/{timestamp}'.format(
        city=invalid_city,
        station=valid_station,
        timestamp=(dt.now() + td(minutes=1)).timestamp()
    ))
    assert json_response(rv)['status'] == 'failure'


def test_api_prediction_invalid_station():
    ''' Check api_prediction returns 'failure' on invalid station '''
    rv = client.get('/api/prediction/{city}/{station}/{timestamp}'.format(
        city=valid_city,
        station=invalid_station,
        timestamp=(dt.now() + td(minutes=1)).timestamp()
    ))
    assert json_response(rv)['status'] == 'failure'


def test_api_prediction_invalid_timestamp():
    ''' Check api_prediction returns 'failure' on invalid timestamp '''
    rv = client.get('/api/prediction/{city}/{station}/{timestamp}'.format(
        city=valid_city,
        station=valid_station,
        timestamp=(dt.now() - td(minutes=1)).timestamp()
    ))
    assert json_response(rv)['status'] == 'failure'


def test_api_prediction_predictions_disabled():
    ''' Check api_prediction returns 'failure' on no predictions enabled '''
    # Tear up
    predictions = tb.read_json(files.predictions)
    predictions[valid_city] = 'No'
    tb.write_json(predictions, files.predictions)
    # Test failure
    rv = client.get('/api/prediction/{city}/{station}/{timestamp}'.format(
        city=valid_city,
        station=valid_station,
        timestamp=(dt.now() - td(minutes=1)).timestamp()
    ))
    assert json_response(rv)['status'] == 'failure'
    # Tear down
    predictions = tb.read_json(files.predictions)
    predictions[valid_city] = 'Yes'
    tb.write_json(predictions, files.predictions)


def test_api_prediction_valid_parameters():
    ''' Check api_prediction returns 'success' on valid parameters '''
    rv = client.get('/api/prediction/{city}/{station}/{timestamp}'.format(
        city=valid_city,
        station=valid_station,
        timestamp=(dt.now() + td(minutes=1)).timestamp()
    ))
    assert json_response(rv)['status'] == 'success'
