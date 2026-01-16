import click
from flask import current_app, Blueprint
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from .model import Base

db_cli = Blueprint("db", __name__)

@db_cli.cli.command("init")
def db_init_command():
    """ Initialize database  """
    db_init()
    click.echo("Initialized the database")

@db_cli.cli.group("db")
def db_group():
    """Database management commands."""
    pass

def db_init():
    """ Initialize Database """
    app = current_app
    db_urn = app.config.get('DB_URN')
    db_user = app.config.get('DB_USER')
    db_pass = app.config.get('DB_PASS')
    db_ip = app.config.get('DB_IP')
    db_name = app.config.get('DB_NAME')

    engine = db_create_engine(db_urn, db_user, db_pass, db_ip, db_name)
    Base.metadata.create_all(engine)

def db_create_engine(urn, db_user, db_pass, db_ip, db_name):
    engine = create_engine(urn.format(db_user, db_pass, db_ip, db_name))

    if not database_exists(engine.url): create_database(engine.url)   

    return engine 
