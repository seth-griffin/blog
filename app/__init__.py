from flask import Flask
import logging
from .extensions import db
from dotenv import load_dotenv
import os


def create_app(dotenv_file=".env"):
    """Create flask application"""

    load_dotenv(dotenv_file)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)8s | %(name)s %(message)s",
    )

    app = Flask(
        __name__,
        static_url_path="/web/",
        static_folder="web/static",
        template_folder="web/templates",
    )

    app.logger.debug("Detailed debug info")
    app.logger.info("Normal operation")
    app.logger.warning("Something suspicious")
    app.logger.error("Something broke")
    app.logger.critical("Requires immediate fixing")

    if "mysql" in os.getenv("DB_URN"):
        uri = "mysql+pymysql://{}:{}@{}:3306/{}".format(
            os.getenv("DB_USER"),
            os.getenv("DB_PASS"),
            os.getenv("DB_IP"),
            os.getenv("DB_NAME"),
        )
    else:
        uri = os.getenv("DB_URN")

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
