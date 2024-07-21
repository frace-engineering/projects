import os


class Config:
    # flask settings
    SECRET_KEY = os.urandom(24).hex()
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://friday:Appoms_db1@localhost/appoms_db"
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True}
    SQLACHEMY_TRACK_MODIFICATIONS = False

    # flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = "Flask-User appoms App"
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = False
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"
    #USER_LOGIN_URL = '/user/login'
