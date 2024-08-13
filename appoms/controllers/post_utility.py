from flask import render_template, redirect, flash, Blueprint, url_for
from appoms import Service, Product, Appointment, db
from flask_login import login_required, current_user
from appoms.form import ServiceForm, AppointmentForm, ProductForm

utility = Blueprint('utility', __name__)

@utility.route('/provider/create_service', methods=['GET', 'POST'])
@login_required
def create_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service_name = form.service_name.data
        description = form.description.data

        new_service = Service(service_name=service_name, user_id=current_user.id, description=description)
        db.session.add(new_service)
        db.session.commit()
        flash('New service entry created', 'success')
        return redirect(url_for('list_utils.list_services'))
    return render_template('utilities/create_service.html', form=form)

@utility.route('/provider/create_product', methods=['GET', 'POST'])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        product_name = form.product_name.data
        model = form.model.data
        yom = form.yom.data
        usage = form.usage.data

        new_product = Product(product_name=product_name, yom=yom, model=model, user_id=current_user.id, usage=usage)
        db.session.add(new_product)
        db.session.commit()
        flash('New product entry created', 'success')
        return redirect(url_for('list_utils.list_products'))
    return render_template('utilities/create_product.html', form=form)

@utility.route('/provider/create_appointment', methods=['GET', 'POST'])
@login_required
def create_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        appointment_date = form.appointment_date.data
        start_time = form.start_time.data
        end_time = form.end_time.data
        notes = form.notes.data

        new_appointment = Appointment(
                appointment_date=appointment_date,
                start_time=start_time,
                end_time=end_time,
                user_id=current_user.id,
                notes=notes
                )
        new_appointment.status = 'open'
        db.session.add(new_appointment)
        db.session.commit()
        flash('New appointment entry created', 'success')
        return redirect(url_for('list_utils.list_appointments'))
    return render_template('utilities/create_appointment.html', form=form)
