import os
import csv

from flask import Blueprint, redirect, url_for 

bp = Blueprint('upload', __name__, url_prefix='/upload')

from teresaefrancisco.models import Product , ProductImage , Contribution , SpecificInfo

@bp.route("/to_csv", methods =["GET", "POST"])
def to_csv():
    models = SpecificInfo.query.first().all_tables_object()
    instances = SpecificInfo.query.first().get_all_tables()
    for model in models.keys():
        models[model] = models[model].__table__.columns.keys()
    for model in instances.keys():
        instances[model] = instances[model].all()

    values = {}
    for model in models.keys():
        values[model] = []
        for instance in instances[model]:
            instance_values = []
            for field in models[model]:
                instance_values.append(getattr(instance, field))
            values[model].append(instance_values)

    for model in models.keys():
        file = os.path.join('teresaefrancisco/static/data/csv', '%s.csv' % model)
        fields = models[model]
        rows = values[model]

        with open(file, 'w') as f:
            write = csv.writer(f)
            
            write.writerow(fields)
            write.writerows(rows)
    return redirect(url_for('main.index'))