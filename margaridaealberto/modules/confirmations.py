from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from teresaefrancisco.tools import tools

from teresaefrancisco.models import Product , Contribution , Confirmation

bp = Blueprint('confirmations', __name__, url_prefix='/confirmations')

@bp.route('/all', methods=('GET', 'POST'))
def all():
    confirmations = Confirmation.query.all()
    return render_template('confirmations/all.html',confirmations=confirmations)

@bp.route('/confirmation', methods=('GET', 'POST'))
def confirmation():
    if request.method == 'POST':
        error = None
        name = request.form.get('name')
        comment = request.form.get('comment')
        is_vegetarian = True if request.form.get('is_vegetarian') == 'True' else False
        has_food_restriction = True if request.form.get('has_food_restriction') == 'True' else False
        food_restriction = request.form.get('food_restriction')

        if not name:
            error = 'Pedimos desculpa, mas precisamos de um nome para poder confirmar a presença'
        if has_food_restriction and not food_restriction:
            error = 'Pedimos desculpa, mas esqueceu-se de indicar que restrição alimentar tem'

        if error is None:
            confirmation = Confirmation(name=name)
            if comment:
                confirmation.comment = comment
            if is_vegetarian:
                confirmation.comment = comment
            if has_food_restriction:
                confirmation.has_food_restriction = has_food_restriction
                confirmation.food_restriction = food_restriction
            confirmation.create()

            return redirect(url_for('confirmations.confirmed'))
        flash(error)
    return render_template('confirmations/confirmation.html')

@bp.route('/confirmed', methods=('GET', 'POST'))
def confirmed():
    return render_template('confirmations/confirmed.html')