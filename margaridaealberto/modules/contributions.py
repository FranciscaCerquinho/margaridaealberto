from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from teresaefrancisco.tools import tools

from teresaefrancisco.models import Product , Contribution

bp = Blueprint('contributions', __name__, url_prefix='/contributions')

@bp.route('/all', methods=('GET', 'POST'))
def all():
    contributions = Contribution.query.all()
    return render_template('contributions/all.html',contributions=contributions)