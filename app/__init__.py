from flask import Flask

""" Create app instance """

app = Flask(__name__,
            static_url_path='/web/',
            static_folder='web/static',
            template_folder='web/templates',
            )

""" Load settings """

app.config.from_pyfile('settings.py')

""" Database module creation"""
from . import routes
from . import db
from .db import db_create_engine 

app.register_blueprint(db.db_cli)

db_urn = app.config.get('DB_URN')
db_user = app.config.get('DB_USER')
db_pass = app.config.get('DB_PASS')
db_ip = app.config.get('DB_IP')
db_name = app.config.get('DB_NAME')

engine = db_create_engine(db_urn, db_user, db_pass, db_ip, db_name)
