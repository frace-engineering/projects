import os


class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://friday:Appoms_db1@localhost/appoms_db"
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    SQLACHEMY_TRACK_MODIFICATIONS = False
