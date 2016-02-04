from flask import render_template
from flask.ext.babel import gettext
from htmlmin import minify
from common import toolbox as tb
from app.views import informationFolder
from app import app


@app.route('/')
def home():
    cities = tb.read_json('{}/cities.json'.format(informationFolder))
    names = tb.read_json('{}/names.json'.format(informationFolder))
    return minify(render_template('index.html',
                                  title=gettext('Maps - OpenBikes'),
                                  cities_file=cities, names_file=names,
                                  lang_code='en'))


@app.route('/<lang_code>')
def index():
    cities = tb.read_json('{}/cities.json'.format(informationFolder))
    names = tb.read_json('{}/names.json'.format(informationFolder))
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
