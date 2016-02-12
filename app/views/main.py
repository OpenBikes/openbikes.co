from flask import render_template
from flask.ext.babel import gettext
from htmlmin import minify
from common import toolbox as tb
from common import files
from app import app


@app.route('/')
@app.route('/index')
def index():
    cities = tb.read_json(files.cities)
    names = tb.read_json(files.names)
    return minify(render_template('index.html', cities_file=cities,
                                  title=gettext('Maps - OpenBikes'),
                                  names_file=names))


@app.route('/api')
def api():
    return minify(render_template('api.html', title=gettext('API - OpenBikes')))


@app.route('/faq')
def faq():
    return minify(render_template('faq.html', title=gettext('FAQ - OpenBikes')))


@app.route('/about')
def about():
    return minify(render_template('about.html', title=gettext('About - OpenBikes')))
