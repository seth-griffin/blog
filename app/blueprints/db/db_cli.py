import click
from flask import current_app as app, Blueprint
from .models import Base
from .util import db_create_engine

db = Blueprint("db", __name__)

@db.cli.command("init")
def db_init_command():
    """Initialize database"""
    db_init()
    click.echo("Initialized the database")


@db.cli.group("db")
def db_group():
    """Database management commands."""
    pass

def db_init():
    """Initialize Database"""
    engine = db_create_engine(
        app.config.get("DB_URN"),
        app.config.get("DB_USER"),
        app.config.get("DB_PASS"),
        app.config.get("DB_IP"),
        app.config.get("DB_NAME"),
    )

    Base.metadata.create_all(engine)
