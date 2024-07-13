from appoms import db, bcrypt
from appoms.models.users import User
from flask_login import current_user, login_user, logout_user, login_required
from flask import Blueprint, flash, url_for, session, request, redirect, render_template, abort
from jinja2 import TemplateNotFound


user_bp = Blueprint("views", __name__)


@user_bp.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def create_user():
    try:
        if request.method == 'POST':
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            password = request.form['password']
            email = request.form['email']
            phone_number = request.form['phone_number']

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            user = User.query.filter_by(username=username).first()
            if user:
                flash("User already exist", "msg")
                return render_template('views/signup.html')
            new_user = User(username=username, first_name=first_name, last_name=last_name,\
                    password=hashed_password, email=email, phone_number=phone_number)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.login'))
        return render_template('views/signup.html')
    except TemplateNotFound:
        abort(404)

@user_bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('pages.home'))
        return render_template('views/login.html')
    except TemplateNotFound:
        abort(404)

