from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session
from .models import Base, Post
from lxml import etree
import os
import datetime


def print_connection_info(session: Session):
    if session is None or session.bind is None:
        print("No active engine / connection right now")
        return

    engine = session.bind  # usually the Engine object
    url = engine.url  # sqlalchemy.engine.URL object

    print("Database URL (masked password):", str(url))
    # Full unmasked version (SQLAlchemy 1.4+ / 2.0+)
    print("Full URL:", url.render_as_string(hide_password=False))

    # Individual components
    print(
        "Dialect / Driver:", url.get_dialect().name, "+", url.drivername.split("+")[-1]
    )
    print("Username:", url.username)
    print("Host:", url.host)
    print("Port:", url.port)
    print("Database name:", url.database)


def db_create_engine(urn, db_user, db_pass, db_ip, db_name):
    engine = create_engine(urn.format(db_user, db_pass, db_ip, db_name))

    if not database_exists(engine.url):
        create_database(engine.url)

    return engine


def data_init(app):
    """Initialize Database"""
    engine = db_create_engine(
        app.config.get("DB_URN"),
        app.config.get("DB_USER"),
        app.config.get("DB_PASS"),
        app.config.get("DB_IP"),
        app.config.get("DB_NAME"),
    )

    Base.metadata.create_all(engine)


def data_clean(db):
    Post.__table__.drop(db.engine)


def data_import_posts(db):
    """Read post flat-files and import into data model"""
    parser = etree.XMLParser(recover=True)

    date_time_format = "%Y-%m-%d"
    posts_base_path = os.getcwd() + "/app/blueprints/data/posts/"
    posts_xml_file_name = "posts.xml"
    posts_xml_data_file_path = posts_base_path + posts_xml_file_name

    tree = etree.parse(posts_xml_data_file_path)
    root = tree.getroot()

    for element in root.iter():

        save = False
        if element.tag == "post":
            post = Post()
        elif element.tag == "id":
            post.id = element.text
        elif element.tag == "categories":
            post.categories = element.text
        elif element.tag == "title":
            post.title = element.text
        elif element.tag == "posted_on":
            post.posted_on = datetime.datetime.strptime(element.text, date_time_format)
        elif element.tag == "content":
            with open(posts_base_path + element.text, "r") as file:
                post.content = file.read()
        elif element.tag == "url_path":
            post.url_path = None
            save = True

        if save == True:
            db.session.add(post)
            print(
                "Attemping to import post with id "
                + post.id
                + " and title "
                + post.title
            )
            try:
                db.session.commit()
                print("Imported!")
            except Exception as e:
                db.session.rollback()
                print(f"An error occurred: {e}")
