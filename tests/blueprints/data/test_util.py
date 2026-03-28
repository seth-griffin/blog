from flask import current_app as app
from app.extensions import db
from sqlalchemy import text
from app.blueprints.data.models import Base, Post
from app.blueprints.data.util import data_clean, data_import_posts
import sqlalchemy


def test_sqlalchemy_database_uri_is_set(app):
    connection_url = app.config["SQLALCHEMY_DATABASE_URI"]

    assert "sqlite" in connection_url
    assert ":memory" in connection_url
    assert "mysql" not in connection_url


def test_data_init(runner):
    data_clean(db)

    # emulate what is done in data_init since it also handles data initialization for the mysql database
    # probably a more elegant way to do this but it should work for now
    Base.metadata.create_all(db.engine)
    post_table_exists_post_init = sqlalchemy.inspect(db.engine).has_table(
        Post.__table__.name
    )
    print(post_table_exists_post_init)
    assert post_table_exists_post_init == True


def test_data_import_posts(runner):
    try:
        Base.metadata.create_all(db.engine)
        data_import_posts(db)
    except SQLAlchemyError as e:
        print("An error occurred:", e)


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
