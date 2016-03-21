import os
from flask import render_template, make_response, send_from_directory
from common import toolbox as tb
from common import files
from app import app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/robots.txt')
def robots_txt():
    return render_template('robots.txt'),
    200, {'Content-type': 'text/plain'}


@app.route('/sitemap.xml')
def sitemap_xml():
    main = ['index', 'faq', 'api', 'about']
    cities = tb.read_json(files.stations).keys()
    sitemap = render_template('sitemap.xml', main=main, cities=cities)
    response = make_response(sitemap)
    response.headers['Content-Type'] = 'application/xml'
    return response
