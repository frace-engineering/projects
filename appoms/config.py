import os


class AppomsConfig:
    SECRET_KEY = os.urandom(24).hex()
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://ugwu:Friday_123@localhost/appoms_db'
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_pre_ping':True}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
