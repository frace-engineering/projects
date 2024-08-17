from flask import render_template, redirect, flash, Blueprint, request, url_for
from appoms import Service, Product, Appointment, User
from sqlalchemy.orm import joinedload
from flask_login import login_required, current_user


list_utils = Blueprint('list_utils', __name__)
@list_utils.route('/services', methods=['GET'])
@login_required
def list_services():
    services = Service.query.all()
    return render_template('utilities/list_services.html', services=services)

@list_utils.route('/products', methods=['GET'])
@login_required
def list_products():
    products = Product.query.all()
    return render_template('utilities/list_products.html', products=products)

@list_utils.route('/appointments', methods=['GET'])
@login_required
def list_appointments():
    appointments = Appointment.query.filter_by(user_id=current_user.id).options(
            joinedload(Appointment.user),
            joinedload(Appointment.service)
            ).all()
    appointment_block = []
    for appointment in appointments:
        client = User.query.filter_by(id=appointment.client_id).first()
        block = {
            "appointment": appointment,
            "provider": appointment.user,
            "client": client,
            "service": appointment.service
            }
        appointment_block.append(block)
    return render_template('utilities/list_appointments.html', appointments=appointment_block)



@list_utils.route('/service', methods=['GET'])
@login_required
def get_service():
    service_name = request.args.get('service_name')
    user_id = request.args.get('user_id')
    if service_name:
        print('Service name:', service_name)
        service = Service.query.filter_by(service_name=service_name).filter_by(user_id=user_id).first()
        return render_template('utilities/service.html', service=service)
    return redirect(request.url)

@list_utils.route('/product', methods=['GET'])
@login_required
def get_product():
    product_name = request.args.get('product_name')
    if product_name:
        product = Product.query.filter_by(product_name=product_name).first()
        return render_template('utilities/product.html', product=product)
    return redirect(request.url)

@list_utils.route('/appointment', methods=['GET'])
@login_required
def get_appointment():
    appointment_date = request.args.get('appointment_date')
    if appointment_date:
        appointment = Appointment.query.filter_by(appointment_date=appointment_date).first()
        return render_template('utilities/appointment.html', appointment=appointment)
    return redirect(request.url)


