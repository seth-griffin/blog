from flask import Flask
from .extensions import db
from dotenv import load_dotenv
import os

def create_app():
    """Create flask application"""
   
    load_dotenv()
    
    app = Flask(
        __name__,
        static_url_path="/web/",
        static_folder="web/static",
        template_folder="web/templates",
    )

    uri = "mysql+pymysql://{}:{}@{}:3306/{}".format(
        os.getenv("DB_USER"),
        os.getenv("DB_PASS"),
        os.getenv("DB_IP"),
        os.getenv("DB_NAME"),
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        "pool_recycle": 3600,
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    """ Load settings """
    app.config.from_object("config.Config")

    """ Import app dependents """
    from .blueprints.blog import routes
    from .blueprints.data import data
    from .blueprints.data.models import Post

    app.register_blueprint(data.data)
    app.register_blueprint(routes.blog)

    @app.template_global("article_link")
    def article_link(post: Post):
        return (
            post.categories.replace(",", "/")
            + "/"
            + post.posted_on.strftime("%Y/%m/%d")
            + "/"
            + post.title.lower().replace(" ", "-")
            + ".html"
        )

    return app
