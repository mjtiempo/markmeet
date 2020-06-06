from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    #initialize the core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    #initialize the plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    with app.app_context():
        #include routes
        #from . import routes
        from .home import home
        from .auth import auth
        from .user import user
        from .meeting import meeting

        #register blueprints
        #app.register_blueprint(admin.admin_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(user.user_bp)
        app.register_blueprint(meeting.meeting_bp)

        return app