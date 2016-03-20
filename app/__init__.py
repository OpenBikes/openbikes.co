from flask import Flask, url_for

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
from app.views import main, map, api, error, seo, locale, redirect
app.register_blueprint(api.apibp)
