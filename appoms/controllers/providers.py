from flask import Blueprint, url_for, redirect, request, render_template, flash
from flask_login import current_user, login_required
from sqlalchemy.orm import joinedload
from appoms import User, Service, Appointment

provider = Blueprint('provider', __name__)

@provider.route('/providers/list', methods=['GET'])
@login_required
def list_providers():
    providers = User.query.filter_by(roles='provider').all()
    if not providers:
        flash('We no service providers listed currently', 'provider-danger')
    else:
        flash('We have the bellow service providers listed', 'provider-success')
    return render_template('users/list_providers.html', providers=providers)


@provider.route('/provider/view', methods=['GET'])
@login_required
def get_provider():
    provider_name = request.args.get('provider_name')
    print(provider_name)
    user = User.query.filter_by(username=provider_name).first()
    provider_services = Service.query.filter_by(user_id=user.id).all()
    print(provider_services)
    if user:
        return render_template('users/provider.html', user=user, services=provider_services)
    flash('Provider not in database', 'danger')
    return "No data too"

@provider.route('/provider/appointments/view', methods=['GET'])
@login_required
def get_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).options(
                joinedload(Appointment.user),
                joinedload(Appointment.service)
            ).all()
    appointment_block = []
    for appointment in appointments:
        client = User.query.filter_by(id=appointment.client_id).first()
        block = {
            "appointment": appointment,
            "provider": current_user,
            "client": client,
            "service": appointment.service
            }
        appointment_block.append(block)
    return render_template('utilities/list_appointments.html', appointments=appointment_block)
