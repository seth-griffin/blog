from flask import Flask
from .extensions import db

def create_app():
    """Create flask application"""
    app = Flask(
        __name__,
        static_url_path="/web/",
        static_folder="web/static",
        template_folder="web/templates",
    )

    uri = "mysql+pymysql://{}:{}@{}:3306/{}".format(
        app.config.get("DB_USER"),
        app.config.get("DB_PASS"),
        app.config.get("DB_IP"),
        app.config.get("DB_NAME")
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = uri 
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        "pool_recycle": 3600
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #db.init_app(db)

    """ Load settings """
    app.config.from_object("config.Config")

    """ Import app dependents """
    from .blueprints.blog import routes
    from .blueprints.db import db_cli

    app.register_blueprint(db_cli.db)
    app.register_blueprint(routes.blog)

    return app
