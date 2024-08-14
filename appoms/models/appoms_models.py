from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime


db = SQLAlchemy()
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(255), nullable=False, default='client')
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    business_name = db.Column(db.String(50), default='')
    business_address = db.Column(db.String(50), default='')
    office_email = db.Column(db.String(50), default='')
    office_phone_number = db.Column(db.String(50), default='')

    appointments = db.relationship('Appointment', back_populates='user', cascade="all, delete-orphan")
    services = db.relationship('Service', back_populates='user', cascade="all, delete-orphan")
    products = db.relationship('Product', back_populates='user', cascade="all, delete-orphan")


    def __repr__(self):
        return f'Username: {self.username}'

    @property
    def role(self):
        return self.roles

    @role.setter
    def role(self, value):
        user_roles = ['client','provider', 'admin']
        if value not in user_roles:
            raise ValueError(f'Role most be one of {user_roles}.')
        self.roles = value


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    yom = db.Column(db.String(50), nullable=False)
    usage = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='products')

    def __repr__(self):
        return f'Product name: {self.product_name}'



class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='services')
    appointments = db.relationship('Appointment', back_populates='service')

    def __repr__(self):
        return f'Service name: {self.service_name}'



class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    appointment_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='open')
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.String(1000), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=True)

    user = db.relationship('User', back_populates='appointments')
    service = db.relationship('Service', back_populates='appointments')


    def __repr__(self):
        return f'Appointment date: {self.appointment_date}'
