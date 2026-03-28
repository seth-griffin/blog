from app.extensions import db
from sqlalchemy import text


def test_sqlite_db_connection(runner):
    result = db.session.query(text("1")).from_statement(text("SELECT 1")).all()
    assert result[0][0] == 1


def test_cmd_create_db_exists(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "create-db" in result.output


def test_cmd_clean_exists(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "clean" in result.output


def test_cmd_import_posts(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "import-posts" in result.output
