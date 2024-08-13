from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, PasswordField, RadioField, TelField
from wtforms import  SelectField, BooleanField, EmailField, MonthField, TextAreaField, DateField, TimeField
from wtforms.validators import DataRequired, InputRequired, Email


class AppomsForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = TelField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


class AppomsProviderForm(FlaskForm):
    business_name = StringField('Business Name', validators=[DataRequired()])
    business_address = StringField('Business address', validators=[DataRequired()])
    office_phone_number = TelField('Office Number', validators=[InputRequired()])
    office_email = EmailField('Office E-mail', validators=[InputRequired(), Email()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('login')


class AppointmentForm(FlaskForm):
    appointment_date = DateField('Appointment date', validators=[DataRequired()])
    start_time = TimeField('Start time', validators=[DataRequired()])
    end_time = TimeField('End time', validators=[DataRequired()])
    notes = TextAreaField('Notes', validators=[DataRequired()])
    submit = SubmitField('Upload')


class ServiceForm(FlaskForm):
    service_name = StringField('Service Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Upload')

class ProductForm(FlaskForm):
    product_name = StringField('Product name', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    yom = MonthField('Year of manufacture', validators=[DataRequired()])
    usage = SelectField('Usage', choices=[('new', 'New'), ('fairly used', 'Fairly Used')])
    submit = SubmitField('Upload')
