from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


def db_create_engine(urn, db_user, db_pass, db_ip, db_name):
    engine = create_engine(urn.format(db_user, db_pass, db_ip, db_name))

    if not database_exists(engine.url):
        create_database(engine.url)

    return engine
