from appoms import db
from flask_login import UserMixin
from .services import Service
from datetime import datetime
from .appointments import Appointment


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    phone_number = db.Column(db.String(255), nullable=False)
    service = db.relationship("Service", back_populates="user", lazy=True)
    appointment = db.relationship("Appointment", back_populates="user")

    def __repr__():
        return f"<User {self.username} {self.first_name}\
                {self.last_name} {self.email} {self.phone_number}>"
