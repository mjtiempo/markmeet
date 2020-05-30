from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#globally accessible libraries
db = SQLAlchemy()

def create_app():
    #initialize the core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    #initialize the plugins
    db.init_app(app)

    with app.app_context():
        #include routes
        #from . import routes
        from .home import home

        #register blueprints
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)
        app.register_blueprint(home.home_bp)

        return app