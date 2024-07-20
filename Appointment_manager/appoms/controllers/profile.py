from flask import redirect, url_for, Blueprint , session
from flask_login import login_required, current_user
from sqlalchemy.exc import OperationalError

profile = Blueprint('profile', __name__)

@profile.route('/user/profile', methods=['GET'], strict_slashes=False)
@login_required
def get_profile():
    if current_user.username in session['usernsme']:
        try:
            username = current_user.username
            profile = Profile.query.filter_by(username=username).first()
            return render_template('profiles/user_profile.html')
        except operationalError:
            flash('Database connection error', 'danger')
            return
        return
    return



