from appoms import db
from flask_user import UserMixin
from .services import Service
from datetime import datetime
from .appointments import Appointment


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information. 'NOCASE' is required to seqrch case insensitively
    # when USER_IFIND_MODE is 'nocase_collation'.
    email = db.Column(db.String(255, collation='utf8_general_ci'), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime()) 
    password = db.Column(db.String(255), nullable=False, server_default='')

    # User information
    username = db.Column(db.String(50, collation='utf8_general_ci'), nullable=False, unique=True)
    first_name = db.Column(db.String(50, collation='utf8_general_ci'), nullable=False)
    last_name = db.Column(db.String(50, collation='utf8_general_ci'), nullable=False)
    business_name = db.Column(db.String(50, collation='utf8_general_ci'), nullable=True)
    business_address = db.Column(db.String(200, collation='utf8_general_ci'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    phone_number = db.Column(db.String(50), nullable=False)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
    authenticated = db.Column(db.Boolean(), default=False)

    # Define the relationship to Service, Role, Appointment
    services = db.relationship("Service", back_populates="users", lazy=True)
    appointment = db.relationship("Appointment", back_populates="user")
    roles = db.relationship("Role", secondary="user_roles")


    def __repr__(self):
        return f"<User {self.username} {self.first_name}\
                {self.last_name} {self.email} {self.phone_number}>"
                
                
    def is_authenticated(self):
        return self.authenticated


# Define the Role data-model
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
