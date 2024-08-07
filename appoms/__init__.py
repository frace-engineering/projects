from flask import Flask
from appoms.config import AppomsConfig
from appoms.models.users import db, User
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager


bcrypt = Bcrypt()
def create_app():
    app = Flask(__name__)
    app.config.from_object(AppomsConfig)
    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager(app)
    login_manager.login_view = 'logbp.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    from appoms.controllers.auth.user import user_bp
    app.register_blueprint(user_bp)

    from appoms.controllers.auth.register import regbp
    app.register_blueprint(regbp)

    from appoms.controllers.auth.login import logbp
    app.register_blueprint(logbp)

    from appoms.controllers.profiles import profile_bp
    app.register_blueprint(profile_bp)

    return app
