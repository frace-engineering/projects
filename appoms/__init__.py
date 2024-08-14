from flask import Flask
from appoms.config import AppomsConfig
from appoms.models.appoms_models import db, User, Product, Service, Appointment
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

    from appoms.controllers.app import appomsbp
    app.register_blueprint(appomsbp)

    from appoms.controllers.auth.register import regbp
    app.register_blueprint(regbp)

    from appoms.controllers.auth.login import logbp
    app.register_blueprint(logbp)

    from appoms.controllers.profiles import profile_bp
    app.register_blueprint(profile_bp)

    from appoms.controllers.post_utility import utility
    app.register_blueprint(utility)

    from appoms.controllers.list_utility import list_utils
    app.register_blueprint(list_utils)

    from appoms.controllers.clients import client
    app.register_blueprint(client)

    from appoms.controllers.providers import provider
    app.register_blueprint(provider)

    return app
