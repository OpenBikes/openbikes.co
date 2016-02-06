from flask import Flask

app = Flask(__name__)

# Setup the application
app.config.from_object('config')

# Add the top level to the import path
import sys
sys.path.append('..')

# Setup Babel
from flask.ext.babel import Babel
babel = Babel(app)

# Import the views
from app.views import main, map, api, error
app.register_blueprint(api.apibp)
