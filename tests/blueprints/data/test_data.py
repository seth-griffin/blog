from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from app.blueprints.data.util import data_clean, data_import_posts
from app.blueprints.data.models import Base


def test_sqlite_db_connection(runner):
    result = db.session.query(text("1")).from_statement(text("SELECT 1")).all()
    assert result[0][0] == 1


def test_data_clean(runner):
    data_clean(db)


def test_data_import_posts(runner):
    try:
        Base.metadata.create_all(db.engine)
        data_import_posts(db)
    except SQLAlchemyError as e:
        print("An error occurred:", e)


def test_cmd_create_db_exists(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "create-db" in result.output


def test_cmd_clean_exists(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "clean" in result.output


def test_cmd_import_posts(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "import-posts" in result.output
