from appoms import Appointment, Service, Product, db, User
from flask import render_template, flash, redirect, request, Blueprint, session, url_for
from flask_login import login_required, current_user


client = Blueprint('client', __name__)

@client.route('/user/appointments', methods=['GET'])
@login_required
def get_user_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    if appointments:
        flash('You have the bellow appointments', 'success')
        return render_template('utilities/list_appointments.html', appointments=appointments)
    return redirect(request.url)

@client.route('/user/appointments/open', methods=['GET'])
@login_required
def get_user_open_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).filter_by(status='open').all()
    if not appointments:
        flash('You have the bellow open appointments to honor.', 'success')
        return render_template('utilities/list_appointments.html', appointments=appointments)

@client.route('/user/appointments/closed', methods=['GET'])
@login_required
def get_user_closed_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).filter_by(status='cloded').all()
    if appointments:
        flash('You have honored the bellow appointments.', 'success')
        return render_template('utilities/list_appointments.html', appointments=appointments)
    return redirect(request.url)

@client.route('/user/free_appointment_slots', methods=['GET', 'POST'])
@login_required
def free_appointment_slots():
    service_name = request.args.get('service_name')
    print(service_name)
    service = Service.query.filter_by(service_name=service_name).first()
    print(service)
    free_slots = Appointment.query.filter_by(status='open').filter_by(user_id=service.user_id).all()
    print(service.id)
    print(service.user_id)
    return render_template('utilities/appointment_slots.html', appointments=free_slots, service=service)


@client.route('/user/book_appointment', methods=['GET', 'POST'])
@login_required
def book_appointment():
    service_id = request.args.get('service_id')
    appointment_id = request.args.get('appointment_id')
    if not service_id or not appointment_id:
        flash('Appointment id and service id are needed', 'danger')
        return render_template('utilities/appointment_slots.html')

    service = Service.query.filter_by(id=service_id).first()
    if not service:
        flash('Service is needed', 'danger')
        return render_template('utilities/appointment_slots.html')

    provider = User.query.filter_by(id=service.user_id).first()
    appointment = Appointment.query.filter_by(id=appointment_id).filter_by(user_id=service.user_id).first()
    if not appointment:
        flash('Appointment is needed', 'danger')
        return render_template('utilities/appointment_slots.html')
    try:
        print(service.id)
        appointment.service_id = service_id
        appointment.status = 'pending'
        db.session.commit()
        flash('You have successfully booked appointment with the bellow detail. Please save the date on a calener', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Something went wrong. Unable to book appointment', 'dager')
    return render_template('utilities/pending_appointments.html', appointment=appointment, service=service, provider=provider, client=current_user)

