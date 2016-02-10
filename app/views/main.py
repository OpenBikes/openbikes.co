from flask import render_template, request, g
from flask.ext.babel import gettext
from htmlmin import minify
from common import toolbox as tb
from common import files
from app import app
from app import babel


@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')


@babel.localeselector
def get_locale():
    ''' Default to english if no lang_code is set. '''
    return g.get('current_lang', 'en')


@app.route('/')
def home():
    cities = tb.read_json(files.cities)
    names = tb.read_json(files.names)
    return minify(render_template('index.html',
                                  title=gettext('Maps - OpenBikes'),
                                  cities_file=cities, names_file=names,
                                  lang_code='en'))


@app.route('/<lang_code>')
def index():
    cities = tb.read_json(files.cities)
    names = tb.read_json(files.names)
    return minify(render_template('index.html',
                                  title=gettext('Maps - OpenBikes'),
                                  cities_file=cities, names_file=names))


@app.route('/<lang_code>/api')
def api():
    return minify(render_template('api.html', title=gettext('API - OpenBikes')))


@app.route('/<lang_code>/faq')
def faq():
    return minify(render_template('faq.html', title=gettext('FAQ - OpenBikes')))


@app.route('/<lang_code>/about')
def about():
    return minify(render_template('about.html', title=gettext('About - OpenBikes')))
