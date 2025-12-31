from flask import Flask

app = Flask(__name__,
            static_url_path='/web/',
            static_folder='web/static',
            template_folder='web/templates',
            )

app.config.from_pyfile('settings.py')

from app import routes
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db_user = app.config.get('DB_USER')
db_pass = app.config.get('DB_PASS')
db_ip = app.config.get('DB_IP')
db_name = app.config.get('DB_NAME')

engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}/'.format(db_user, db_pass, db_ip, db_name))

if not database_exists(engine.url): create_database(engine.url)
