from flask import (Blueprint, flash, g, redirect, render_template, request,
                   url_for)
from werkzeug.exceptions import abort

from cannalysis_api.db import get_db

bp = Blueprint('requester', __name__)


@bp.route('/')
def index():
    return render_template('requester/index.html')


@bp.route('/new', methods=('GET', 'POST'))
def new():
    if request.method == 'POST':
        request_string = request.form['request_string']
        error = None

        if not request_string:
            error = 'Request string is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO metrc_reqs (request_string)'
                       ' VALUES (?)', (request_string))
            db.commit()
            return redirect(url_for('requests.history'))
    return render_template('requests/new.html')


@bp.route('/history')
def history():
    db = get_db()
    reqs = db.execute(
        'SELECT r.id, request_string, created'
        ' FROM metrc_reqs p JOIN metrc_resp resps ON r.request_string = resps.request_string'  # noqa
        ' ORDER BY created DESC').fetchall()
    return render_template('requests/history.html', requests=reqs)
