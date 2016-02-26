from flask import g, abort
from app import app
from app import babel


@babel.localeselector
def get_locale():
    ''' Retrieve the language code from the HTTP request header. '''
    return g.get('lang_code', app.config['DEFAULT_LOCALE'])


@app.url_defaults
def set_language_code(endpoint, values):
    ''' Inject the language code into a call for url_for() automatically. '''
    if 'lang_code' in values or not g.get('lang_code', None):
        return
    if app.url_map.is_endpoint_expecting(endpoint, 'lang_code'):
        values['lang_code'] = g.lang_code


@app.url_value_preprocessor
def get_lang_code(endpoint, values):
    '''
    Obtain and set the language code from the request on the application globals
    flask.g object.
    '''
    if values is not None:
        g.lang_code = values.pop('lang_code', app.config['DEFAULT_LOCALE'])


@app.before_request
def ensure_lang_support():
    ''' Check the requested language is supported. '''
    lang_code = g.get('lang_code', None)
    if lang_code and lang_code not in app.config['SUPPORTED_LANGUAGES'].keys():
        return abort(404)
