A README.md file for Appointment manager web application project.

Installation:
To install and run the application on your local machine, you have to either fork or clone the repository on you localhost.

$ git clone https://github.com/frace-engineering/projects.git

This project is in the development stage
set up a python virtual environment 
If you already have venv installed
$ python3 -m venv <your-virtual-environment-name>
$ . <your-virtual-environment-name>/bin/activate or
$ source <your-virtual-environment-name>/bin/activate

If you dont have venv installed already, you can install it using this command
$ pip install python3-env

cd to the root of the project and run
$ pip install -e .  # to install the required dependencies for the project.

After a successfull installation, it is time to start the application.

$ flask --app appoms --debug  # You may wish to omit the --debug flag

After a successfull startup, visit the page in your browser through http://localhost:5000/


Don't forget to that the application has to be hooked to a sql database. 
This current version is on mysql.
