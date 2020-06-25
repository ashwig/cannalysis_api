from flask import (  # noqa: F401
    Blueprint, flash, g, redirect, render_template, request,
    url_for)  # noqa: F401
from werkzeug.exceptions import abort  # noqa: F401

from cannalysis_api.db import get_db

bp = Blueprint('requester', __name__)


@bp.route('/requester')
def index():
    return render_template('requester/index.html')


def get_metrc_resp_history(id, check_history):
    metrc_resp = get_db().execute(
        'SELECT resp.id, result_code, license_facility, id_number,'
        ' last_modified_date, tag_number, request_string, json_body, created'
        ' FROM response resp JOIN request req ON resp.created = req.created'
        ' WHERE resp.id = ?', (id, )).fetchone()

    if metrc_resp is None:
        flash('No requests made yet! Please create a new one.')
        return render_template('requester/empty.html')

    return metrc_resp


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
            db.execute('INSERT INTO metrc_resps')
            db.commit()
            return redirect(url_for('requester.history'))
    return render_template('requester/new.html')


@bp.route('/requester/history')
def history():
    db = get_db()
    metrc_resps = db.execute(
        'SELECT resps.id, result_code, license_facility, id_number,'
        ' last_modified_date, tag_number, resps.request_string, json_body,'
        ' resps.created'
        ' FROM metrc_resps resps JOIN metrc_reqs reqs ON resps.created ='
        ' reqs.created'
        ' ORDER BY resps.created DESC').fetchall()

    if len(metrc_resps) == 0:
        flash('No requests found.')

    return render_template('requester/history.html',
                           metrcresponses=metrc_resps)
