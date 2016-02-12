from flask import request, g
from app import app
from app import babel


@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        print(user.locale)
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


@app.before_request
def before_request():
    ''' Store global variables to use all over the application. '''
    # Storing the locale for modifying the HTML templates
    g.locale = get_locale()
