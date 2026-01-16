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
    from .blueprints.blog import routes
    from .blueprints.db import db_cli    
#from .blueprints.blog.routes import blog
    #from .blueprints.db import db_cli
    
    app.register_blueprint(db_cli.db)
    app.register_blueprint(routes.blog)
    
    return app
