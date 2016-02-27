from flask import redirect, url_for
from app import app

@app.route('/')
@app.route('/index')
def redirect_index():
    return redirect(url_for('index'))
