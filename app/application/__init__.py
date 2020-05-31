from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    #initialize the core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    #initialize the plugins
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        #include routes
        #from . import routes
        from .home import home
        from .auth import auth

        #register blueprints
        #app.register_blueprint(admin.admin_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(auth.auth_bp)

        return app