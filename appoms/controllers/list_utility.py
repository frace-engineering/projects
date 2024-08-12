from flask import render_template, redirect, flash, Blueprint, request
from appoms import Service, Product, Appointment
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
    appointments = Appointment.query.all()
    return render_template('utilities/list_appointments.html', appointments=appointments)



@list_utils.route('/service', methods=['GET'])
@login_required
def get_service():
    service_name = request.args.get('service_name')
    if service_name:
        service = Service.query.filter_by(service_name=service_name).first()
        return render_template('utilities/service.html', service=service)
    return refirect(url_for('list_services'))

@list_utils.route('/product', methods=['GET'])
@login_required
def get_product():
    product = request.args.get('product_name')
    return render_template('utilities/product.html', product=product)

@list_utils.route('/appointment', methods=['GET'])
@login_required
def get_appointment():
    appointment = request.args.get('appointment_date')
    return render_template('utilities/appointment.html', appointment=appointment)


