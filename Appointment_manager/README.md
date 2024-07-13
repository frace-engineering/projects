
  POST-ALX-SE PORTFOLIO PROJECT.

The appointment management application is built to help user manage their daily tight schedule.

Reason for the project:
  - to consolidate on the user authentication concept in python

Technologies used:
 - Python
 - flask
 - mysql
 - alembic

Package and dependency installation:
 Python3 came preinstalled in ubuntu
create a virtual python environmnt inside the project directory.
 $ python3 -m venv env # this will create the virtual env and activate it.

 $ source env/bin/actiate
 
 $ python3 -m pip install flask flask-sqlalchemy flask-bcrypt flask-login alembic flask-migrate
 $ python3 -m pip freeze > requirements.txt

The above instructions install the required packages then copy the packages and dependencies for the application into requirements.txt file.The requirements.txt file ensures that the development environment/dependencies is mirroed.

To regenarate the exact environment you run 
  $ python3 -m pip install -r requirements.txt

Take a peep into the requirement.txt

# reruirements.st

alembic==1.13.2
bcrypt==4.1.3
blinker==1.8.2
click==8.1.7
flask==3.0.3
Flask-Bcrypt==1.0.1
Flask-Login==0.6.3
Flask-Migrate==4.0.7
flask-sqlalchemy==3.1.1
greenlet==3.0.3
gunicorn==22.0.0
importlib-metadata==8.0.0
importlib-resources==6.4.0
itsdangerous==2.2.0
jinja2==3.1.4
Mako==1.3.5
MarkupSafe==2.1.5
mysql-connector-python==9.0.0
packaging==24.1
SQLAlchemy==2.0.31
typing-extensions==4.12.2
werkzeug==3.0.3
zipp==3.19.2



