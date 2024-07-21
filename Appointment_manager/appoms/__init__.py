from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_user import UserManager
from flask_bcrypt import Bcrypt
from .config import Config
from flask_migrate import Migrate


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
user_manager = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'user.login'

    from .models.users import User
    global user_manager
    user_manager = UserManager(app, db, User)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



    with app.app_context():
        db.create_all()

    from .pages import bp as pages_bp
    app.register_blueprint(pages_bp)

    from .controllers.users import user_bp
    app.register_blueprint(user_bp)

    from .controllers.services import user_bp
    app.register_blueprint(user_bp)

    from .controllers.profile import profile
    app.register_blueprint(profile)


    return app
