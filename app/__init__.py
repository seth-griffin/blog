from flask import Flask

app = Flask(__name__,
            static_url_path='/web/',
            static_folder='web/static',
            template_folder='web/templates',
            )

from app import routes
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db_user = 'dev'
db_pass = ''
db_ip = 'localhost'
db_name = 'blog'
engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}/'.format(db_user, db_pass, db_ip, db_name))

if not database_exists(engine.url): create_database(engine.url)
