from setuptools import setup, find_packages

setup(
        name="appoms",
        version="0.1.0",
        packages=find_packages(),
        install_requires=[
            "flask",
            "flask-login",
            "flask-babel",
            "flask-bcrypt",
            "flask-sqlalchemy",
            "mysql-connector-python",
            "email-validator",
            "flask-migrate",
            "alembic",
            "flask-wtf",
            "datetime"
            ]
        )

        
