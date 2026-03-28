from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session 

def print_connection_info(session: Session):
    if session is None or session.bind is None:
        print("No active engine / connection right now")
        return

    engine = session.bind               # usually the Engine object
    url = engine.url                    # sqlalchemy.engine.URL object

    print("Database URL (masked password):", str(url))
    # Full unmasked version (SQLAlchemy 1.4+ / 2.0+)
    print("Full URL:", url.render_as_string(hide_password=False))

    # Individual components
    print("Dialect / Driver:", url.get_dialect().name, "+", url.drivername.split("+")[-1])
    print("Username:", url.username)
    print("Host:", url.host)
    print("Port:", url.port)
    print("Database name:", url.database)



def db_create_engine(urn, db_user, db_pass, db_ip, db_name):
    engine = create_engine(urn.format(db_user, db_pass, db_ip, db_name))

    if not database_exists(engine.url):
        create_database(engine.url)

    return engine
