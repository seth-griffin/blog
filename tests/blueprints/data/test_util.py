from app.extensions import db
from sqlalchemy import text
from app.blueprints.data.models import Post
from app.blueprints.data.util import data_clean
import sqlalchemy


def test_sqlalchemy_database_uri_is_set(app):
    connection_url = app.config["SQLALCHEMY_DATABASE_URI"]

    assert "sqlite" in connection_url
    assert ":memory" in connection_url
    assert "mysql" not in connection_url


def test_data_clean(app):
    post_table_exists_pre_clean = sqlalchemy.inspect(db.engine).has_table(
        Post.__table__.name
    )
    data_clean(db)
    post_table_exists_post_clean = sqlalchemy.inspect(db.engine).has_table(
        Post.__table__.name
    )

    assert post_table_exists_pre_clean == True
    assert post_table_exists_post_clean == False


def test_db_session(app):
    assert db.session.is_active
    assert db.session.execute(text("SELECT 1"))
