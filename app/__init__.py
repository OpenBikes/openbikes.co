from flask import Flask, request, g

app = Flask(__name__)

# Setup the application
app.config.from_object('config')

# Add the top level to the import path
import sys
sys.path.append('..')

# Setup Babel
from flask.ext.babel import Babel
babel = Babel(app)

@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')

@babel.localeselector
def get_locale():
    return g.get('current_lang', 'en')

# Import the views
from app.views import main, map, api, error
app.register_blueprint(api.apibp)
