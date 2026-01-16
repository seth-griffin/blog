from flask import Flask

def create_app():
    """ Create flask application """
    app = Flask(
        __name__,
        static_url_path="/web/",
        static_folder="web/static",
        template_folder="web/templates",
    )

    """ Load settings """
    app.config.from_object("config.Config")

    """ Import app dependents """
    from .blueprints.routes import routes
    from .blueprints.routes.routes import blog
    from .blueprints.db import db
    from .blueprints.db.db import db_create_engine
    
    app.register_blueprint(db.db_cli)
    app.register_blueprint(blog)

    #engine = db_create_engine(
    #    app.config.get("DB_URN"),
    #    app.config.get("DB_USER"),
    #    app.config.get("DB_PASS"),
    #    app.config.get("DB_IP"),
    #    app.config.get("DB_NAME")
    #)
    
    return app
