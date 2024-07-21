from appoms import db
from appoms.models.users import User, Role
from flask_login import current_user, login_user, logout_user, login_required
from flask import Blueprint, flash, url_for, session, request, redirect, render_template, abort
from jinja2 import TemplateNotFound
from flask_user import roles_required
from appoms import user_manager

user_bp = Blueprint("views", __name__)


@user_bp.route('/')
def index():
    return render_template('pages/home.html', current_user=current_user)

@user_bp.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def create_user():
    try:
        if request.method == 'POST':
            user_role = Role.query.filter_by(name='user').first()
            if not user_role:
                user_role = Role(name='user')
                db.session.add(user_role)
                db.session.commit()

            user_role = Role(name='user')
            username = request.form['username']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            password = request.form['password']
            email = request.form['email']
            phone_number = request.form['phone_number']

            hashed_password = user_manager.hash_password(password)

            user = User.query.filter_by(username=username).first()
            if user:
                flash("User already exist", "msg")
                return render_template('views/signup.html')
            user_role = Role.query.filter_by(name='user').first()
            new_user = User(username=username, first_name=first_name, last_name=last_name,\
                    password=hashed_password, email=email, phone_number=phone_number, roles=[user_role,], active=True)
            db.session.add(new_user)
            db.session.commit()
            return render_template('views/roles.html')
        return render_template('views/signup.html')
    except TemplateNotFound:
        abort(404)

@user_bp.route('/user/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = User.query.filter_by(email=email).first()
            if user and user_manager.verify_password(password, user.password):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return render_template('views/user_home.html')
        return render_template('views/login.html')
    except TemplateNotFound:
        abort(404)

@user_bp.route('/users', methods=['GET'], strict_slashes=False)
@login_required
def users():
    try:
        users = User.query.all()
        if users:
            return render_template('views/list_users.html', users=users)
        flash('No user found', 'danger')
        return render_template('views/user_home.html')
    except TemplateNotFound:
        abort(404)

@user_bp.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.commit()
    logout_user()
    flash('Successfully logged out', 'success')
    return redirect(url_for('views.login'))


@user_bp.route('/provider_role', methods=['GET', 'POST'])
def create_provider_role():
    if request.method == 'POST':
        business_name = request.form['business_name']
        business_address = request.form['business_address']
        current_user.business_name = business_name
        current_user.business_address = business_address
        provider_role = Role.query.filter_by(name='provider').first()
        current_user.roles = [provider_role,]
        db.session.commit()
        return redirect(url_for('viewa.login'))
    return render_template('views/providers.html')

@user_bp.route('/user_role')
def create_user_role():
    return redirect(url_for('views.login'))

