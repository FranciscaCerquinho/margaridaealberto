import os

from flask import Flask
from tempfile import mkdtemp
from flask_session import Session

from . import sql_db
from . import modules
from teresaefrancisco.tools import specific_info
from teresaefrancisco.models import SpecificInfo

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    database_path = 'sqlite:///' + app.root_path + '/database.db'

    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # Ensure responses aren't cached
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    @app.before_first_request
    def before_first_request():
        modules.startup.add_to_session()
    
    @app.context_processor
    def inject_to_template():
        info = SpecificInfo.query.first()
        if not info:
            information = {
                'title': specific_info.title,
                'mbway1': specific_info.mbway1,
                'mbway2': specific_info.mbway2,
                'iban': specific_info.iban,
            }
            info = SpecificInfo(name=specific_info.name,information=information)
            info.create()
        return {'information': info.information}

    # Configure session to use filesystem (instead of signed cookies)
    app.config["SESSION_FILE_DIR"] = mkdtemp()
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    if test_config is None:
        # Load the instance config when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        # Load the test config
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(modules.main.bp)
    app.register_blueprint(modules.api.bp)
    app.register_blueprint(modules.upload.bp)
    app.register_blueprint(modules.products.bp)
    app.register_blueprint(modules.contributions.bp)
    app.register_blueprint(modules.honeymoon.bp)
    app.register_blueprint(modules.edit.bp)
    app.register_blueprint(modules.create.bp)
    app.register_blueprint(modules.confirmations.bp)
    with app.app_context():
        sql_db.db.init_app(app)
        sql_db.db.create_all()

    return app