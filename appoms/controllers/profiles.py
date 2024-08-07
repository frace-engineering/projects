from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from appoms.form import LoginForm
from appoms import bcrypt, User


profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/user/profile', methods=['GET'])
@login_required
def get_user_profile():
    user = current_user
    fname = user.first_name
    lname = user.last_name
    full_name = lname + ' ' + fname
    return render_template('profile.html', user=user, full_name=full_name)

@profile_bp.route('/user/profile', methods=['GET'])
@login_required
def update_profile():
    user = current_user
    fname = user.first_name
    lname = user.last_name
    full_name = lname + fname
    return render_template('profile.html', user=user, full_name=full_name)
