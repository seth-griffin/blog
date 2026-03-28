import click
from flask import current_app as app, Blueprint
from .util import data_init, data_clean, data_import_posts
from ...extensions import db

data = Blueprint("data", __name__)


@data.cli.command("create-db")
def data_init_command():
    """Initialize database"""
    data_init(app)
    click.echo("Initialized the database")


@data.cli.command("clean")
def data_clean_command():
    data_clean(db)
    print("Database dropped and data deleted")


@data.cli.command("import-posts")
def data_populate_data_command():
    """Populate database with pre-defined posts"""
    data_import_posts(db)
    click.echo("Posts populated")
