import os
import unidecode

from flask import Blueprint, flash, g, redirect, render_template, request, url_for , current_app
from werkzeug.security import check_password_hash, generate_password_hash
from teresaefrancisco.tools import tools

from teresaefrancisco.models import Product , Contribution , ProductImage , Confirmation , SpecificInfo

bp = Blueprint('edit', __name__, url_prefix='/edit')

@bp.route('/products', methods=('GET', 'POST'))
def products():
    products = Product.query.all()
    return render_template('edit/products.html',products=products)

@bp.route('/product/<product_id>', methods=('GET', 'POST'))
@bp.route('/product/<product_id>/<delete>', methods=('GET', 'POST'))
def product(product_id,delete=None):
    product = Product.query.filter_by(id=product_id).first()
    if request.method == 'POST':
        if delete=='delete':
            product.delete()
        else:
            name = request.form.get('name')
            description = request.form.get('description')
            price = float(request.form.get('price')) if request.form.get('price') else None
            store = request.form.get('store')
            show_price = True if request.form.get('show_price') else False
            priority = int(request.form.get('priority')) if request.form.get('priority') else None
            images_to_delete = request.form.getlist('images_to_delete')
            id_of_images_to_delete = [int(id) for id in images_to_delete]

            values = {
                'name':name,
                'description':description,
                'price':price,
                'store':store,
                'show_price':show_price,
                'priority':priority
            }
            product.update_with_dict(values)
            
            files = request.files.getlist('pictures')

            num_of_images = len(product.images)

            for index in range(len(files)):
                file = files[index]
                if file.filename != '':
                    image_name = str(product.name).replace(" ", "").lower()
                    image_name = unidecode.unidecode(image_name)

                    filename = os.path.join('images','products','{image_name}{index}.jpg'.format(image_name=image_name,index=index+num_of_images))
                    path = current_app.root_path + url_for('static', filename = filename)
                    file_exists = os.path.exists(path)
                    if not file_exists:
                        img_file = open(path,'wb')
                        img_file.close()
                    file.save(path)

                    new_image = ProductImage(path=filename)

                    new_image.product = product
                    new_image.create()

            for id in id_of_images_to_delete:
                image = ProductImage.query.filter_by(id=id).first()
                image.delete()
        return redirect(url_for('edit.products'))

    return render_template('edit/product.html',product=product)

@bp.route('/contributions', methods=('GET', 'POST'))
def contributions():
    contributions = Contribution.query.all()
    return render_template('edit/contributions.html',contributions=contributions)

@bp.route('/contribution/<contribution_id>', methods=('GET', 'POST'))
@bp.route('/contribution/<contribution_id>/<delete>', methods=('GET', 'POST'))
def contribution(contribution_id,delete=None):
    contribution = Contribution.query.filter_by(id=contribution_id).first()
    if request.method == 'POST':
        if delete=='delete':
            contribution.delete()
        else:
            name = request.form.get('name')
            value_contributed =  float(request.form.get('value_contributed')) if request.form.get('value_contributed') else None
            message = request.form.get('message')
            product = Product.query.filter_by(id=int(request.form.get('product'))).first() if request.form.get('product') else None

            values = {
                'name':name,
                'value_contributed':value_contributed,
                'message':message,
                'product':product
            }
            contribution.update_with_dict(values)

        return redirect(url_for('edit.contributions'))

    products = Product.query.all()

    return render_template('edit/contribution.html',contribution=contribution,products=products)

@bp.route('/confirmations', methods=('GET', 'POST'))
def confirmations():
    confirmations = Confirmation.query.all()
    return render_template('edit/confirmations.html',confirmations=confirmations)

@bp.route('/specific_info', methods=('GET', 'POST'))
def specific_info():
    specific_info = SpecificInfo.query.first()
    if request.method == 'POST':
        title = request.form.get('title')
        mbway1 = request.form.get('mbway1')
        mbway2 = request.form.get('mbway2')
        iban = request.form.get('iban')
        information = {
            'title':title,
            'mbway1':mbway1,
            'mbway2':mbway2,
            'iban':iban
        }
        specific_info.information = information
        specific_info.save()
        return redirect(url_for('edit.specific_info'))
    return render_template('edit/specific_info.html',specific_info=specific_info)