from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user
from appoms import db, bcrypt, User
from appoms.form import AppomsForm


regbp = Blueprint('regbp', __name__)

@regbp.route('/register', methods=['POST', 'GET'])
def register():
    form = AppomsForm()
    if form.validate_on_submit():
        username = form.username.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        email = form.email.data
        phone_number = form.phone_number.data

        user = User.query.filter_by(username=username).first()
        if user:
            flash(f'Username <{user.username}'.upper() + '> already taken. Please chose another username.', 'danger')
            return redirect(url_for('regbp.register'))
        hash_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                password=hash_pwd
                )
        db.session.add(new_user)
        db.session.commit()
        flash(f'User <{new_user.username}'.upper() + '> created successfully. Please login to access your page.', 'success')
        return redirect(url_for('logbp.login'))
    return render_template('register.html', form=form)
