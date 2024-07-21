from flask import Blueprint, render_template, redirect, request, abort, url_for, flash
from appoms.models.services import Service
from flask_login import login_required, current_user
from flask_user import roles_required
from appoms import db
from jinja2 import TemplateNotFound

user_bp = Blueprint('user', __name__)

@user_bp.route('/create_service', methods=['GET', 'POST'], strict_slashes=False)
#@roles_required('provider')
def create_service():
    if request.method == 'POST':
        try:
            service_name = request.form['service_name']
            description = request.form['description']

            new_service = Service(service_name=service_name, description=description, user_id=current_user.id)
            db.session.add(new_service)
            db.session.commit()
            flash('Service created successfuly', 'success')
            return redirect(url_for('user.list_services'))
        except TemplateNotFound:
            abort(404)
    return render_template('views/create_service.html')

@user_bp.route('/services', methods=['GET'], strict_slashes=False)
@login_required
def list_services():
    try:
        services = Service.query.all()
        if services:
            flash('Fetched sercices successfully', 'success')
            return render_template('view_services/list_services.html', services=services)
        flash("Couldn't fetch services", "danger")
        return redirect(url_for('user.list_services'))
    except TemplateNotFound:
        abort(404)

@user_bp.route('/services/<string:service_name>', methods=['GET'], strict_slashes=False)
@login_required
def services(service_name):
    try:
        services = Service.query.filter_by(service_name=service_name).all()
        if services:
            flash('Fetched sercices successfully', 'success')
            return render_template('view_services/list_services.html', services=services)
        flash("Couldn't fetch services", "danger")
        return redirect(url_for('user.list_services'))
    except TemplateNotFound:
        abort(404)
