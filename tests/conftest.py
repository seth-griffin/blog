import pytest
from app import create_app
from app.extensions import db
from app.blueprints.data.util import print_connection_info
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.blueprints.data.models import Base
from app.blueprints.data.data import data_import_posts


@pytest.fixture
def app():
    app = create_app(".env_test")

    ctx = app.app_context()
    ctx.push()

    with app.app_context():
        result = db.session.query(text("1")).from_statement(text("SELECT 1")).all()
        assert result[0][0] == 1
        try:
            Base.metadata.create_all(db.engine)
            data_import_posts(db)
        except SQLAlchemyError as e:
            print("An error occurred:", e)
            exit()

    yield app

    with app.app_context():
        db.drop_all()
        db.session.remove()

    print_connection_info(db.session)
    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
