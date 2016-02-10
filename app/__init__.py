from flask import Flask

app = Flask(__name__)

# Setup the application
app.config.from_object('app.config')

# Add the top level to the import path
import sys
sys.path.append('..')

# Setup Babel
from flask.ext.babel import Babel
babel = Babel(app)

# Import the views
from app.views import main, map, api, error
app.register_blueprint(api.apibp)

# Cache
from flask.ext.cache import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Sitemap
from functools import wraps
from flask_sitemap import Sitemap, sitemap_page_needed

@sitemap_page_needed.connect
def create_page(app, page, urlset):
    cache[page] = sitemap.render_page(urlset=urlset)

def load_page(fn):
    @wraps(fn)
    def loader(*args, **kwargs):
        page = kwargs.get('page')
        data = cache.get(page)
        return data if data else fn(*args, **kwargs)
    return loader

app.config['SITEMAP_MAX_URL_COUNT'] = 10
app.config['SITEMAP_VIEW_DECORATORS'] = [load_page]

sitemap = Sitemap(app=app)
