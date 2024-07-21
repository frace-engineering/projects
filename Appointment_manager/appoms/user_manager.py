from flask_user import UserManager
from .models.users import User
from appoms import db, create_app

app = create_app()
user_manager = UserManager(app, db, User)
