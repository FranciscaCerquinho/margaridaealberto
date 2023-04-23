from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from teresaefrancisco.tools import tools

from teresaefrancisco.models import Product , Contribution


bp = Blueprint('honeymoon', __name__, url_prefix='/honeymoon')

@bp.route('/all', methods=('GET', 'POST'))
@bp.route('/all/<update>', methods=('GET', 'POST'))
def all(update=None):    
    products = Product.query.filter_by(show_price=True).all()
    if update == 'update':
        for product in products:
            product.update_price_paid()
    products_paid = [product for product in products if product.is_paid()]
    products = [product for product in products if not product.is_paid()]
    #products = list(set(products) - set(products_paid))
    return render_template('honeymoon/all.html',products=products,products_paid=products_paid)

@bp.route('/product/<product_id>', methods=('GET', 'POST'))
@bp.route('/product/<product_id>/<contribution_id>', methods=('GET', 'POST'))
def product(product_id,contribution_id=None):
    product = Product.query.filter_by(id=product_id).first()
    contribution=None
    if contribution_id:
        contribution = Contribution.query.filter_by(id=contribution_id).first()

    ##VERFICAR SE A CONTRIBUICAO FOI DESTE PRODUTO
    if request.method == 'POST':
        error = None
        name = request.form.get('name')
        value_contributed_original = request.form.get('value_to_contribute')
        value_contributed = float(value_contributed_original) if tools.is_float(value_contributed_original) else None
        message = request.form.get('message')

        if not name:
            error = 'Pedimos desculpa, mas precisamos de um nome para poder registar a contribuição'
        if not value_contributed_original:
            error = 'Pedimos desculpa, mas precisamos de um valor para poder registar a contribuição'
        if not value_contributed:
            error = 'Pedimos desculpa, mas o valor precisa de ser escrito só com números'

        if error is None:
            contribution = Contribution(name=name,value_contributed=value_contributed,product_id=product.id)
            if message:
                contribution.message = message
            contribution.create()

            product.price_paid += value_contributed
            product.save()

            return redirect(url_for('honeymoon.product',product_id=product.id,contribution_id=contribution.id))
        flash(error)
    return render_template('honeymoon/product.html',product=product,contribution=contribution)
