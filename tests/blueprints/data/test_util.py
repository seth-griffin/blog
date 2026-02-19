from app.blueprints.data.util import db_create_engine

def test_is_using_in_memory_db(db_engine):
    connection_url = str(db_engine.url)

    assert "sqlite" in connection_url
    assert ":memory" in connection_url
    assert "mysql" not in connection_url
