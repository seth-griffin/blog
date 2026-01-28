import click
import os
from flask import current_app as app, Blueprint
from .models import Base
from .util import db_create_engine
from lxml import etree
from .models import Post

db = Blueprint("db", __name__)

@db.cli.command("create-db")
def db_init_command():
    """Initialize database"""
    db_init()
    click.echo("Initialized the database")

@db.cli.command("populate-posts")
def db_populate_data_command():
    """Populate database with pre-defined posts"""
    db_populate_posts()
    click.echo("Posts populated")


def db_populate_posts():
    """Read post flat-files and import into data model"""
    db = SQLAlchemy()
    parser = etree.XMLParser(recover=True)
    
    posts_base_path = os.getcwd() + "/app/blueprints/db/posts/"
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
            post.posted_on = element.text
        elif element.tag == "content":
            with open(posts_base_path + "/" + element.text, "r") as file:
                post.content = file.read()
                post.content = element.text
        elif element.tag == "url_path":
            post.content = None 
            save = True
        
        if save == True:
            db.session.add(post)
            print("Attemping to import post with id " + post.id + "and title " + post.title)
            try:
                db.session.commit()
                print("Imported!")
            except Exception as e:
                db.session.rollback()
                print(f"An error occurred: {e}") 


@db.cli.group("db")
def db_group():
    """Database management commands."""
    pass


def db_init():
    """Initialize Database"""
    engine = db_create_engine(
        app.config.get("DB_URN"),
        app.config.get("DB_USER"),
        app.config.get("DB_PASS"),
        app.config.get("DB_IP"),
        app.config.get("DB_NAME"),
    )

    Base.metadata.create_all(engine)

