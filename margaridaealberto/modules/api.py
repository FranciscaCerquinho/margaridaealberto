import functools
import os
import csv

from flask import Blueprint, flash, g, jsonify, redirect, render_template, request, current_app, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from teresaefrancisco.tools import tools
from teresaefrancisco.model import Model
from teresaefrancisco.models import Product , Confirmation , SpecificInfo

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/create/<table_name>', methods=('GET', 'POST'))
def create(table_name=None):
    columns = {}
    if table_name:
        columns = Model.get_columns_names_types_from_name(Model,table_name)
    tables = Model.get_tables(Model)
    return render_template('api/create.html',tables=tables,columns=tools.convert_type_to_html_input(columns))

@bp.route('/delete_confirmation/<id>', methods=('GET', 'POST'))
def delete_confirmation(id):
    confirmation = Confirmation.query.filter_by(id=id).first()

    if confirmation:
        confirmation.delete()
    return redirect(url_for('confirmations.all'))

@bp.route("/to_csv/<model>", methods =["GET", "POST"])
def to_csv(model):
    models = SpecificInfo.query.first().all_tables_object()
    instances = SpecificInfo.query.first().get_all_tables()
    if not model in models.keys():
        return "Model not found"

    fields = models[model].__table__.columns.keys()
    instances[model] = instances[model].all()

    values = {}
    values[model] = []
    for instance in instances[model]:
        instance_values = []
        for field in fields:
            instance_values.append(getattr(instance, field))
        values[model].append(instance_values)

    filename = 'data/csv/%s.csv' % model
    file = current_app.root_path + url_for('static', filename = filename)
    rows = values[model]

    with open(file, 'w') as f:
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(rows)
    return jsonify({"status": "success"})
