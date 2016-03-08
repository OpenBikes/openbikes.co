from flask import render_template
from app import app


@app.errorhandler(403)
def interfit(e):
    return render_template('error.html', message='403 forbidden',
                           title='{} - OpenBikes'.format(403)), 403


@app.errorhandler(404)
def page_non_trouvee(e):
    return render_template('error.html', message='404 not found',
                           title='{} - OpenBikes'.format(404)), 404


@app.errorhandler(410)
def ne_fonctionne_plus(e):
    return render_template('error.html', message='410 not working',
                           title='{} - OpenBikes'.format(410)), 410


@app.errorhandler(500)
def erreur_interne(e):
    return render_template('error.html', message='500 server error',
                           title='{} - OpenBikes'.format(500)), 500
