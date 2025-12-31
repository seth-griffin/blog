from flask import Blueprint
import click

db_cli = Blueprint("db", __name__)

@db_cli.cli.group("db")
def db_group():
    """Database management commands."""
    pass

@db_cli.cli.command("init")
def init():
    """ Initialize Database """
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    init_db()
    click.echo('Initialized the database')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def create_app():
    app = Flask(__name__)
    from . import db
    db.init_app(app)

    return app
