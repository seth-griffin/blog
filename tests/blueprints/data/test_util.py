
def test_sqlalchemy_database_uri_is_set(app):
    connection_url = app.config["SQLALCHEMY_DATABASE_URI"] 

    assert "sqlite" in connection_url
    assert ":memory" in connection_url
    assert "mysql" not in connection_url
