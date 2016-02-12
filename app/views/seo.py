from flask import render_template
from common import toolbox as tb
from common import files
from app import app


@app.route('/robots.txt')
def robots_txt():
    return render_template('robots.txt'), 200, {'Content-type': 'text/plain'}


@app.route('/sitemap.xml')
def sitemap_xml():
    main = ['index', 'api', 'faq', 'about']
    cities = tb.read_json(files.stations).keys()
    return render_template('sitemap.xml', main=main, cities=cities),
    200, {'Content-type': 'text/xml;charset=utf-8'}
