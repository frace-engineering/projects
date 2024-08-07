from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user
from appoms.form import LoginForm
from appoms import bcrypt, User


logbp = Blueprint('logbp', __name__)

@logbp.route('/user/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash(f'Welcome to your page, {user.username}.', 'success')
            return redirect(url_for('profile_bp.get_user_profile'))
        flash('Oops! email and password error. Please supply your correct detail.', 'danger')
    return render_template('login.html', form=form)
